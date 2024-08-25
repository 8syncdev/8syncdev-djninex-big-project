from .model import (
    Permission,
    Group,
    User,
    ContentType,
)
from .schema import (
    PermissionSchema,
    GroupSchema,
)


from api_core.dev import (
    #^ Async custom
    alist,
    sta,
)

from api_core.common.type import *

class PermissionService:

    def __init__(self):
        self.model = Permission

    async def get_all_permissions_of_users(self):
        all_users: List[User] = await alist(
            await sta(User.objects.all)()
        )
        data = []
        for user in all_users:
            all_pers: List[str] = await alist(
                await sta(user.get_all_permissions)()
            )
            print(all_pers)
            data.append({
                'user': user.username,
                'permissions': all_pers
            })

        return data
    
    async def get_all(self):
        try:
            all_permissions = await alist(
                await sta(self.model.objects.all)()
            )
            return [PermissionSchema.from_orm(permission) for permission in all_permissions]
        except Exception as e:
            return f"Failed to get all permissions, {e}"
        
    async def create_permission_for_user_model(self, permission: PermissionSchema):
        try:
            content_type = ContentType.objects.get_for_model(User)
            created_permission = await self.model.objects.acreate(**permission.dict(), content_type=content_type)
            return PermissionSchema.from_orm(created_permission)
        except Exception as e:
            return f"Failed to create permission, {e}"
        
    async def add_permission_to_user(self, username: str, permission_codename: str):
        try:
            user = await User.objects.aget(username=username)
            permission = await self.model.objects.aget(codename=permission_codename)
            await user.user_permissions.aadd(permission)
            await user.asave()
            return {
                'username': user.username,
                'permission': permission.codename
            }
        except Exception as e:
            return f"Failed to add permission to user, {e}"
        
    async def check_permission(self, username: str, permission_codename: str):
        try:
            user = await User.objects.aget(username=username)
            has_permission = await sta(user.has_perm)(permission_codename)

            return {
                'username': user.username,
                'permission': permission_codename,
                'has_permission': has_permission
            }
        except Exception as e:
            return f"Failed to check permission, {e}"
    
    async def delete_permission(self, codename: str):
        try:
            permission = await self.model.objects.aget(codename=codename)
            await permission.adelete()
            return {
                'codename': codename
            }
        except Exception as e:
            return f"Failed to delete permission, {e}"
    
    async def delete_permission_from_user(self, username: str, permission_codename: str):
        try:
            user = await User.objects.aget(username=username)
            permission = await self.model.objects.aget(codename=permission_codename)
            await user.user_permissions.aremove(permission)
            await user.asave()
            return {
                'username': user.username,
                'permission': permission.codename
            }
        except Exception as e:
            return f"Failed to delete permission from user, {e}"