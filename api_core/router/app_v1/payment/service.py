from api_core.common.type import *

from api_core.dev import (
    #^ Async custom
    alist,
    sta,
    alist_model,
    afilter
)

from .model import *

from django.utils.timezone import timedelta, now

class PaymentService:

    def __init__(self):
        self.payment_model = Payment
        self.user_enrollment_model = UserEnrollment
        self.user_model = User
    
    async def get_payments(self):
        payments = await alist_model(self.payment_model.objects.all)
        return payments
    
    async def get_all_payments_by_user(self, user_id: int=None, user: User = None):
        if user_id is None and user is None:
            return []
        if user_id is not None:
            print(user_id)
            payments = await afilter(
                func=self.payment_model.objects.select_related('user').filter,
                user__pk=user_id
            )
        elif user is not None:
            print(user)
            payments = await afilter(
                func=self.payment_model.objects.select_related('user').filter,
                user=user
            )
        return payments
    
    async def create_payment_by_user(self, user_id: int = None, user: User = None):
        if user_id is None and user is None:
            return {
                'user_id': user_id,
                'amount': 0,
                'status': Payment.STATUS_PENDING,
                'courses': []
            }
        
        if user_id is not None:
            get_all_user_enrollment_enrolled = await afilter(
                func=self.user_enrollment_model.objects.select_related('user', 'course').filter,
                user__pk=user_id,
                status__in=[UserEnrollment.STATUS_ENROLLED, UserEnrollment.STATUS_TRIAL, UserEnrollment.STATUS_EXPIRED] # TODO: kết thúc trial để thanh toán
            )
        elif user is not None:
            get_all_user_enrollment_enrolled = await afilter(
                func=self.user_enrollment_model.objects.select_related('user', 'course').filter,
                user=user,
                status__in=[UserEnrollment.STATUS_ENROLLED, UserEnrollment.STATUS_TRIAL, UserEnrollment.STATUS_EXPIRED]
            )
        if get_all_user_enrollment_enrolled.__len__() == 0:
            return {
                'user_id': user_id if user_id is not None else user.pk,
                'amount': 0,
                'status': Payment.STATUS_PENDING,
                'courses': []
            }
        sum_price = 0
        for user_enrollment in get_all_user_enrollment_enrolled:
            sum_price += user_enrollment.course.price
            user_enrollment.status = UserEnrollment.STATUS_PENDING
            await user_enrollment.asave()
            
        payment = await self.payment_model.objects.acreate(
            user=await self.user_model.objects.aget(pk=user_id if user_id is not None else user.pk),
            amount=sum_price,
            status=Payment.STATUS_PENDING,
            message=[
                {
                    'course': user_enrollment.course.pk,
                    'user_enrollment': user_enrollment.pk,
                    'course_name': user_enrollment.course.name,
                    'course_img_url': user_enrollment.course.img_url,
                    'price': user_enrollment.course.price,
                }
                for user_enrollment in get_all_user_enrollment_enrolled
            ]
        )
        
        return {
            'user': user_id if user_id is not None else user.pk,
            'amount': payment.amount,
            'status': payment.status,
            'courses': payment.message
        }
    
    async def get_payment_pending_by_user_id(self, user_id: int):
        payments = await afilter(
            func=self.payment_model.objects.select_related('user').filter,
            user__pk=user_id,
            status=Payment.STATUS_PENDING
        )

        return payments
    
    async def delete_all_payments(self):
        await self.payment_model.objects.all().adelete()
        return {
            'message': 'Delete all payments success'
        }
    
    async def done_payment(self, user_id: int = None, user: User = None, payment_id: int = None):
        if payment_id is not None:
            payment = await self.payment_model.objects.select_related('user').aget(
                pk=payment_id
            )
            payments = [payment]
        elif user_id is not None:
            payments = await afilter(
                func=self.payment_model.objects.select_related('user').filter,
                user__pk=user_id,
                status=Payment.STATUS_PENDING
            )
        elif user is not None:
            payments = await afilter(
                func=self.payment_model.objects.select_related('user').filter,
                user=user,
                status=Payment.STATUS_PENDING
            )
        
        if payments.__len__() == 0:
            return {
                'message': 'Payment not found'
            }

        for payment in payments:
            for message in payment.message:
                user_enrollment = await self.user_enrollment_model.objects.select_related('user', 'course').aget(
                    pk=message.get('user_enrollment')
                )
                user_enrollment.status = UserEnrollment.STATUS_COMPLETED
                user_enrollment.expiration_date = now() + timedelta(days=UserEnrollment.EXPIRATION_DAYS)
                await user_enrollment.asave()

        payment.status = Payment.STATUS_COMPLETED
        await payment.asave()

        return {
            'message': 'Done payment success'
        }

    