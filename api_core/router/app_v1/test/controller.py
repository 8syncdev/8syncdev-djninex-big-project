from api_core.common.restfull import *
from .service import (
    populate_database,
    delete_all
)



@api_controller(
    prefix_or_class='/test-appv1',
)
class TestAppv1Controller:

    def __init__(self):
        pass

    @route.get(
        path='/create-realdata',
    )
    def create_realdata(self):
        try:
            populate_database()
            return {
                'message': 'Populated database successfully'
            }
        except Exception as e:
            return {
                'message': str(e)
            }
    
    @route.get(
        path='/delete-all',
    )
    def delete_all(self):
        try:
            delete_all()
            return {
                'message': 'Deleted all data successfully'
            }
        except Exception as e:
            return {
                'message': str(e)
            }