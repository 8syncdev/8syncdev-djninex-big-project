from .user import (
    ClientUserController,
    AdminUserController
)
from .permission import (
    PermissionController
)
from .test import (
    TestAppv1Controller
)

from .course import (
    CourseController
)

from .payment import (
    PaymentController
)


ALL_ROUTERS_APP_V1 = [
    #^ User
    ClientUserController,
    AdminUserController,
    #^ Permission
    PermissionController,
    #^ Test
    TestAppv1Controller,
    #^ Course
    CourseController,
    #^ Payment
    PaymentController,
]