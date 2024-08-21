from .user import (
    ClientUserController,
    AdminUserController
)
from .permission import (
    PermissionController
)


ALL_ROUTERS_APP_V1 = [
    #^ User
    ClientUserController,
    AdminUserController,
    #^ Permission
    PermissionController
]