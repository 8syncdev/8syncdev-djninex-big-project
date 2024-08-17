
'''
    Author: Nguyễn Phương Anh Tú
    Date created: 12/08/2024 (Vietnam format)
    Exp: 3 exp of Django, DRF, Nin, FastAPI, NestJS Backend Developer
    Contact: 0767449819
    Working on: 
        - Freelancer
        - Department: 
            - T3H Co. Ltd.
            - Công ty Cổ Phần Điện Lực Minh Khang.
            - Co-Leader of Teaching Assistant.
'''
# from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI
from api_core.dev import (
    CustomTokenObtainPairController
)
from .router import (
    ALL_ROUTERS_APP_V1
)
from ninja_jwt.controller import NinjaJWTDefaultController


api = NinjaExtraAPI(
    title='API Core',
    version='1.0.0',
    description='''
    API Core for Django Ninja Extra
    Devloped by: Nguyễn Phương Anh Tú
''',
    docs_url='/docs',
)

api.register_controllers(
    *ALL_ROUTERS_APP_V1,
    CustomTokenObtainPairController,
    # NinjaJWTDefaultController,
)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', api.urls),
]
