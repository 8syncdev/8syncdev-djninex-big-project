from api_core.common.restfull import *
from .service import (
    populate_database,
    delete_all,
    populate_data
)



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
            populate_database(records_per_model=10)
            return {
                'message': 'Populated database successfully'
            }
        except Exception as e:
            return {
                'message': str(e)
            }
        
    @route.get(
        path='/create-testdata-manual',
    )
    def create_testdata(self):
        try:
            populate_data()
            return {
                'message': 'Created test data successfully'
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