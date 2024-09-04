from ninja import ModelSchema, Schema

from .model import (
    Payment,
    UserEnrollment, 
)

class PaymentOutputSchema(ModelSchema):
    class Meta:
        model = Payment
        fields = (
            'amount',
            'status',
            'date',
            'user',
            'message',
        )