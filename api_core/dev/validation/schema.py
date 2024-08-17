from ninja import (
    ModelSchema,
    Schema,
)
from typing import (
    Any,
    Union,
)


class ValidationSuccessSchema(Schema):
    success: bool
    detail: Union[str, dict, list[dict], Any]

class ValidationFailedSchema(Schema):
    success: bool
    detail: Union[str, dict, list[dict], Any]

    

