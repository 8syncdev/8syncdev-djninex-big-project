from api_core.common.restfull import *
from .service import (
    delete_all,
)
from gen_db import TestDB



@api_controller(
    prefix_or_class='/test-appv1',
    tags=['Test Appv1'],
)
class TestAppv1Controller:

    def __init__(self):
        pass

    @route.get(
        path='/create-realdata-fakerlib',
    )
    def create_realdata(self):
        try:
            TestDB.create_all_data()
            return {
                'success': 'Done'
            }

        except Exception as e:
            return  {
                'error': str(e)
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
        

