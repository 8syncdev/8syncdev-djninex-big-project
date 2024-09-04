from ninja_extra.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    BasePermission,
    IsAuthenticatedOrReadOnly,
)

from ninja_extra import permissions

from app_v1.models import *

from api_core import Request

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.method in permissions.SAFE_METHODS
    

class UserWithPermission(permissions.BasePermission):
    def __init__(self, permission: str) -> None:
        self._permission = permission

    def has_permission(self, request: Request, view):
        return request.user.has_perm(self._permission)


