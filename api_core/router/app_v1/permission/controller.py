from api_core.common.restfull import *
from .service import (
    PermissionService,
)



@api_controller(
    prefix_or_class="/permission",
    tags=["Permission"],
    auth=AsyncJWTAuth(),
    permissions=[IsAuthenticated & IsAdminUser],
)
class PermissionController:
    
    def __init__(self,
                    permission_service: PermissionService):
            self.permission_service = permission_service

    @route.get("/all-pers-of-users")
    @paginate_dev()
    async def get_all_permissions_of_users(self, request: Request):
        try: 
            res = await self.permission_service.get_all_permissions_of_users()
            return res
        except Exception as e:
            return res_invalid(f"Failed to get all permissions of users, {e}")
    
    @route.get("/all")
    @paginate_dev()
    async def get_all(self, request: Request):
        try:
            res = await self.permission_service.get_all()
            return res 
        except Exception as e:
            return res_invalid(f"Failed to get all permissions, {e}")
    

    @route.get(
        path='/check-permission-by-request',
        summary='Check permission of user auto by request',
        permissions=[IsAuthenticated & UserWithPermission('app_v1.add_address')],
        auth=AsyncJWTAuth(),
    )
    async def check_permission_req(self, request):
        try:
            res = request.user.has_perm('app_v1.add_address')
            return res_valid(res)
        except Exception as e:
            return res_invalid(f"Failed to check permission, {e}")
    
    @route.get(
        path='/check-permission',
        summary='Check permission of user',
    )
    async def check_permission_data(self, username: str, permission: str):
        try:
            res = await self.permission_service.check_permission(username, permission)
            return res_valid(res)
        except Exception as e:
            return res_invalid(f"Failed to check permission, {e}")
        
    @route.post(
        path='/add-permission-to-user',
        summary='Add permission to user',
    )
    async def add_permission_to_user(self, request, username: str, permission: str):
        try:
            res = await self.permission_service.add_permission_to_user(username, permission)
            return res_valid(res)
        except Exception as e:
            return res_invalid(f"Failed to add permission to user, {e}")
        
    @route.post(
        path='/delete-permission-from-user',
        summary='Delete permission from user',
    )
    async def delete_permission_from_user(self, request, username: str, permission: str):
        try:
            res = await self.permission_service.delete_permission_from_user(username, permission)
            return res_valid(res)
        except Exception as e:
            return res_invalid(f"Failed to delete permission from user, {e}")