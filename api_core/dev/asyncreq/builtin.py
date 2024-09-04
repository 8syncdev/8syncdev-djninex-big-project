from asgiref.sync import sync_to_async as sta
from typing import (
    List,
    Any,
    Callable,
    TypeVar,
    Awaitable,
    Generic,
    Union
)

from django.db.models import QuerySet


T = TypeVar('T')

# Định nghĩa hàm alist với kiểu trả về là List[T]
def alist(args: List[T]) -> List[T]:
    return sta(list)(args)

# Định nghĩa hàm alist_model với kiểu trả về là List[T]
async def alist_model(func: Callable[[], QuerySet[T]]) -> List[T]:
    '''
        Tham số: func=name_model.objects.all #^ truyền hàm
    '''
    return await alist(
        await sta(func)()
    )

async def afilter(func: Callable[[], QuerySet[T]], *args, **kwargs) -> List[T]:
    return await alist(
        await sta(func)(*args, **kwargs)
    )