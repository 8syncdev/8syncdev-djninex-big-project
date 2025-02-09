from api_core.common.restfull import *
from .service import (
    PermissionService,
)



@api_controller(
    prefix_or_class="/permissions",
    tags=["Permission"],
    auth=AsyncJWTAuth(),
    permissions=[IsAuthenticated & IsAdminUser],
)
class PermissionController:
    
    def __init__(self,
                    permission_service: PermissionService):
            self.permission_service = permission_service

    @route.get("/users")
    @paginate_dev()
    async def get_all_permissions_of_users(self, request: Request):
        try: 
            res = await self.permission_service.get_all_permissions_of_users()
            return res
        except Exception as e:
            return res_invalid(f"Failed to get all permissions of users, {e}")
    
    @route.get("")
    @paginate_dev()
    async def get_all(self, request: Request):
        try:
            res = await self.permission_service.get_all()
            return res 
        except Exception as e:
            return res_invalid(f"Failed to get all permissions, {e}")
    

    @route.get(
        path='/check',
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
        path='/verify',
        summary='Check permission of user',
    )
    async def check_permission_data(self, username: str, permission: str):
        '''
        Example:
        - username: admin
        - permission: admin.add_address
        '''
        try:
            res = await self.permission_service.check_permission(username, permission)
            return res_valid(res)
        except Exception as e:
            return res_invalid(f"Failed to check permission, {e}")
        
    @route.post(
        path='/assign',
        summary='Add permission to user',
    )
    async def add_permission_to_user(self, request, username: str, permission: str):
        '''
        Example:
        - username: admin
        - permission: add_address
        '''
        try:
            res = await self.permission_service.add_permission_to_user(username, permission)
            return res_valid(res)
        except Exception as e:
            return res_invalid(f"Failed to add permission to user, {e}")
        
    @route.post(
        path='/revoke',
        summary='Delete permission from user',
    )
    async def delete_permission_from_user(self, request, username: str, permission: str):
        '''
        Example:
        - username: admin
        - permission: add_address
        '''
        try:
            res = await self.permission_service.delete_permission_from_user(username, permission)
            return res_valid(res)
        except Exception as e:
            return res_invalid(f"Failed to delete permission from user, {e}")