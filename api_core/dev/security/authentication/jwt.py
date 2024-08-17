from ninja_jwt.controller import (
    AsyncNinjaJWTSlidingController,
    AsyncNinjaJWTDefaultController,
    AsyncTokenBlackListController,
)
from ninja_extra import (
    api_controller,
)
from ninja_extra.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)

@api_controller(
    prefix_or_class='/token',
    tags=['Authentication JWT Token'],
    permissions=[AllowAny],
)
class CustomTokenObtainPairController(AsyncNinjaJWTDefaultController): ...
    

