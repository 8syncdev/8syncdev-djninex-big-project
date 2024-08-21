from .schema import (
    ValidationFailedSchema,
    ValidationSuccessSchema,
)

from typing import (
    Union
)

def res_valid(data: Union[dict, list[dict]]) -> ValidationSuccessSchema:
    '''
        Don't accept string as data
    '''
    try:
        if isinstance(data, str):
            return ValidationFailedSchema(success=False, detail=data)
        else:
            return ValidationSuccessSchema(success=True, detail=data)
    except Exception as e:
        return ValidationFailedSchema(success=False, detail=f"Failed to create response, {e}")

def res_invalid(data: Union[str, dict, list[dict]]) -> ValidationFailedSchema:
    try:
        return ValidationFailedSchema(success=False, detail=data)
    except Exception as e:
        return ValidationFailedSchema(success=False, detail=f"Failed to create response, {e}")