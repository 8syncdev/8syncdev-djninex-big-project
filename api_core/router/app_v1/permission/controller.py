from api_core.common.restfull import *
from .service import (
    PermissionService,
)



@api_controller(
    prefix_or_class="/permission",
    tags=["Permission"],
    # auth=AsyncJWTAuth(),
    # permissions=IsAdminUser,
)
class PermissionController:
    
    def __init__(self,
                    permission_service: PermissionService):
            self.permission_service = permission_service

    @route.get("/all-pers-of-users")
    @paginate_dev()
    async def get_all_permissions_of_users(self, request: Request):
        return await self.permission_service.get_all_permissions_of_users()
    
    @route.get("/all")
    @paginate_dev()
    async def get_all(self, request: Request):
        return await self.permission_service.get_all()