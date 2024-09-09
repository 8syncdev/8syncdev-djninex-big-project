from ninja import ModelSchema, Schema

from .model import (
    Payment,
    UserEnrollment, 
)

class PaymentOutputSchema(ModelSchema):
    class Meta:
        model = Payment
        fields = (
            'id',
            'amount',
            'status',
            'date',
            'user',
            'message',
        )


