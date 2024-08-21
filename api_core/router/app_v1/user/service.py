from .model import User
from .schema import (
    ClientUserOutputSchema,
    ClientUserInputSchema,
    AdminUserOutputSchema,
    UpdateClientUserInputSchema,
)

from api_core.common.type import *

from api_core.dev import (
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
                return ("Username and password cannot be 'string'")
            created_user = await self.model.objects.acreate(**user.dict())
            created_user.set_password(user.password)
            await created_user.asave()
            return ClientUserOutputSchema.from_orm(created_user)
        except Exception as e:
            return (f"Failed to create user, {e}")
           
    async def update_current_user(self, current_user: User, user: UpdateClientUserInputSchema):
        try:
            if current_user.username != user.username:
                return ("Username didn't match with current user")
            for key, value in user.dict().items():
                if value == 'string':
                    continue
                setattr(current_user, key, value) if key != 'password' else current_user.set_password(value)
            await current_user.asave()
            return (ClientUserOutputSchema.from_orm(current_user))
        except Exception as e:
            return (f"Failed to update user, {e}")
    
    #^ Admin service
    async def get_all(self):
        try:
            all_users = await alist(
                await sta(self.model.objects.all)()
            )
            return [AdminUserOutputSchema.from_orm(user) for user in all_users]
        except Exception as e:
            return f"Failed to get all users, {e}"

       
    
    