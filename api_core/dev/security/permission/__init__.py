from ninja_extra.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    BasePermission,
    IsAuthenticatedOrReadOnly,
)


from .custom import (
    ReadOnly,
    UserWithPermission,
)