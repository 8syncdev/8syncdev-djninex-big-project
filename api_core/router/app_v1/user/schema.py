from .model import User
from ninja import (
    ModelSchema,
)

class ClientUserInputSchema(ModelSchema):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

class UpdateClientUserInputSchema(ModelSchema):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        )
       

class ClientUserOutputSchema(ModelSchema):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone',
            'first_name',
            'last_name',
        )

class AdminUserOutputSchema(ModelSchema):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone',
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
            'last_login',
        )