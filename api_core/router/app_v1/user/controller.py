from api_core.common.restfull import *

from .schema import (
    ClientUserInputSchema,
    ClientUserOutputSchema,
    AdminUserOutputSchema,
    UpdateClientUserInputSchema,
)

from .service import (
    UserService,
)



@api_controller(
    prefix_or_class='/user',
    tags=['Client User API'],
)
class ClientUserController:
    '''
        ClientUserController:
            - role base on Django User model: user, superuser, staff
    '''
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    # @route.get('/', response=PaginatedResponseSchema)
    # @paginate_dev()
    # async def get_all(self, request):
    #     all_users = await self.user_service.get_all()
    #     return all_users
    
    @route.post(
        path='',
        summary='Create a new user',
    )
    async def create(self, request, user: ClientUserInputSchema):
        '''
        # Docs English:
        ## Create a new user

        Parameter:
        - user: ClientUserInputSchema

        Return:
        - ClientUserOutputSchema
        '''
        try:
            data = await self.user_service.create(user)
            return res_valid(data)
        except Exception as e:
            return res_invalid(f"Failed to create user, {e}")
    
    @route.post(
        path='/edit', 
        summary='Edit information of current user',
        response=Union[
            ClientUserOutputSchema,
            Any
        ], 
        permissions=[IsAuthenticated], 
        auth=AsyncJWTAuth()
    )
    async def update(self, request, edited_user: UpdateClientUserInputSchema):
        try:
            data = await self.user_service.update_current_user(request.user, edited_user)
            return res_valid(data)
        except Exception as e:
            return res_invalid(f"Failed to update user, {e}")
    

@api_controller(
    prefix_or_class='/admin',
    tags=['Admin User API'],
    permissions=[IsAdminUser],
    auth=AsyncJWTAuth(),
)
class AdminUserController:
    def __init__(self, 
                 user_service: UserService
                 ):
        self.user_service = user_service

    @route.post(
        path='/user',
        summary='Create a new user',
    )
    async def create(self, request, user: ClientUserInputSchema):
        '''
        # Docs English:
        ## Create a new user

        Parameter:
        - user: ClientUserInputSchema

        Return:
        - ClientUserOutputSchema
        '''
        try:
            data = await self.user_service.create(user)
            return res_valid(data)
        except Exception as e:
            return res_invalid(f"Failed to create user, {e}")
            
    @route.post(
        path='/user/edit', 
        summary='Edit information of current user',
        response=Union[
            ClientUserOutputSchema,
            Any
        ], 
        permissions=[IsAuthenticated], 
        auth=AsyncJWTAuth()
    )
    async def update(self, request, edited_user: UpdateClientUserInputSchema):
        try:
            data = await self.user_service.update_current_user(request.user, edited_user)
            return res_valid(data)
        except Exception as e:
            return res_invalid(f"Failed to update user, {e}")
    
    @route.get(
        path='/user',
        summary='Get all users',
        response=PaginatedResponseSchema,
    )
    @paginate_dev()
    async def get_all(self, request):
        try:
            all_users = await self.user_service.get_all()
            return all_users
        except Exception as e:
            return res_invalid(f"Failed to get all users, {e}")