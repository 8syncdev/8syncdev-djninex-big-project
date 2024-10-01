from api_core.common.restfull import *
from .service import (
    delete_all,
)
from gen_db import TestDB

from api_core import DEBUG



@api_controller(
    prefix_or_class='/test-appv1',
    tags=['Test App v1'],
)
class TestAppv1Controller:
    ...
    def __init__(self):
        pass

    @route.get(
        path='/create-all-data',
    )
    def create_all_data(self):
        try:
            TestDB.create_all_data() if DEBUG else None
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
            delete_all() if DEBUG else None
            return {
                'message': 'Deleted all data successfully'
            }
        except Exception as e:
            return {
                'message': str(e)
            }
        

