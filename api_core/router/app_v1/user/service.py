from .model import User
from .schema import (
    ClientUserOutputSchema,
    ClientUserInputSchema,
    AdminUserOutputSchema,
    UpdateClientUserInputSchema,
)

from typing import (
    Union,
    Literal,
)

from api_core.dev import (
    res_invalid,
    res_valid,
    ValidationFailedSchema,
    ValidationSuccessSchema,
    #^ Async custom
    alist,
    sta,
)


#^ Define types
RoleUserType = Literal['user', 'superuser', 'staff']


#^ Define Dependency Injection Class
class UserService:
    def __init__(self):
        self.model = User

    async def create(self, user: ClientUserInputSchema):
        try:
            if user.username == 'string' or user.password == 'string':
                return res_invalid("Username and password cannot be 'string'")
            created_user = await self.model.objects.acreate(**user.dict())
            created_user.set_password(user.password)
            await created_user.asave()
            return ClientUserOutputSchema.from_orm(created_user)
        except Exception as e:
            return res_invalid(f"Failed to create user, {e}")
           
    async def update_current_user(self, current_user: User, user: UpdateClientUserInputSchema):
        try:
            if current_user.username != user.username:
                return res_invalid("Username cannot be changed")
            for key, value in user.dict().items():
                if value == 'string':
                    continue
                setattr(current_user, key, value) if key != 'password' else current_user.set_password(value)
            await current_user.asave()
            return res_valid(ClientUserOutputSchema.from_orm(current_user))
        except Exception as e:
            return res_invalid(f"Failed to update user, {e}")
    
    #^ Admin service
    async def get_all(self):
        try:
            all_users = await alist(
                await sta(self.model.objects.all)()
            )
            return [AdminUserOutputSchema.from_orm(user) for user in all_users]
        except Exception as e:
            return res_invalid(f"Failed to get all users, {e}")

       
    
    