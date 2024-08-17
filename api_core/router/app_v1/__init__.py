from .user import (
    ClientUserController,
    AdminUserController
)


ALL_ROUTERS_APP_V1 = [
    #^ User
    ClientUserController,
    AdminUserController
]