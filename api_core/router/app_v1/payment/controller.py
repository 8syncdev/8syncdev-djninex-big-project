from api_core.common.restfull import *

from .service import (
    PaymentService,
)

from .schema import (
    PaymentOutputSchema,
)

from .model import (
    User
)

from typing import Optional



@api_controller(
    prefix_or_class='/payment',
    tags=['Payment'],
)
class PaymentController:

    def __init__(self, payment_service: PaymentService):
        self.payment_service = payment_service

    @route.get(
        path='',
        summary='Get all payments',
    )
    @paginate_dev()
    async def get_all(self, request):
        try:
            data = await self.payment_service.get_payments()
            return [PaymentOutputSchema.from_orm(payment) for payment in data]
        except Exception as e:
            return res_invalid(f'Get all payments failed: {e}')
        
    @route.get(
        path='/user',
        summary='Get all payments by user',
        auth=AsyncJWTAuth(),
    )
    @paginate_dev()
    async def get_all_payments_by_user(self, request: Request, user_id: Optional[int] = None):
        try:
            params = {
                'user_id': user_id,
                'user': request.user,
            } if request.user.is_superuser else {
                'user': request.user,
            }
            data = await self.payment_service.get_all_payments_by_user(**params)
            return [PaymentOutputSchema.from_orm(payment) for payment in data]
        except Exception as e:
            return res_invalid(f'Get all payments by user failed: {e}')
        
    @route.post(
        path='/user',
        summary='Create payment by user',
        auth=AsyncJWTAuth(),
        permissions=[IsAuthenticated]
    )
    async def create_by_user(self, request: Request, user_id: Optional[int] = None):
        try:
            params = {
                'user_id': user_id,
                'user': request.user,
            } if request.user.is_superuser else {
                'user': request.user,
            }
            data = await self.payment_service.create_payment_by_user(**params)
            return data
        except Exception as e:
            return res_invalid(f'Create payment by user failed: {e}')
        
    @route.get(
        path='/user/{user_id}/pending',
        summary='Get payment pending by user',
    )
    @paginate_dev()
    async def get_payment_pending_by_user(self, request, user_id: int):
        try:
            data = await self.payment_service.get_payment_pending_by_user_id(user_id)
            return [PaymentOutputSchema.from_orm(payment) for payment in data]
        except Exception as e:
            return res_invalid(f'Get payment pending by user failed: {e}')
        


    @route.delete(
        path='',
        summary='Delete all payments',
    )
    async def delete_all(self, request):
        try:
            data = await self.payment_service.delete_all_payments()
            return res_valid(data)
        except Exception as e:
            return res_invalid(f'Delete all payments failed: {e}')
        
    @route.post(
        path='/done',
        summary='Done payment by user',
        auth=AsyncJWTAuth(),
        permissions=[IsAuthenticated, IsAdminUser]
    )
    async def done_payment(self, request: Request, user_id: Optional[int] = None, payment_id: Optional[int] = None):
        try:
            params = {
                'user_id': user_id,
                'payment_id': payment_id,
                'user': request.user,
            }
            data = await self.payment_service.done_payment(**params)
            return data
        except Exception as e:
            return res_invalid(f'Done payment failed: {e}')
        
        
    