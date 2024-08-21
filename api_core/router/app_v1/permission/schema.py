from ninja import (
    ModelSchema,
    Schema,
)

from .model import *

class PermissionSchema(ModelSchema):
    class Meta:
        model = Permission
        exclude = ['id']

class GroupSchema(ModelSchema):
    class Meta:
        model = Group
        exclude = ['id']

class UserSchema(ModelSchema):
    class Meta:
        model = User
        exclude = ['id']

