from ninja_extra import (
    api_controller,
    route,
)
from ninja_jwt.authentication import AsyncJWTAuth

from api_core.dev import (
    #^ Pagination
    paginate_dev,
    PaginatedResponseSchema,
    #^ Permission
    IsAuthenticated,
    IsAdminUser,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)


from typing import (
    Union,
    Any
)