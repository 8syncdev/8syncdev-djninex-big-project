from ninja_extra.pagination import (
    paginate, 
    PageNumberPaginationExtra, PaginatedResponseSchema,
    PaginationBase
)

from typing import Any, List

from pydantic import Field
from ninja import Schema


class CustomPagination(PageNumberPaginationExtra):
    class Input(Schema):
        page: int = Field(1, gt=0)
        page_size: int = Field(10, lt=11)


def paginate_dev(
    class_pagination: PaginationBase = CustomPagination,
    _page_size: int = 10
):
    return paginate(
        class_pagination,
        page_size=_page_size,
    )
