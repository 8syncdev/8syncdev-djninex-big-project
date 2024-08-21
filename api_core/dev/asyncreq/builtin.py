from asgiref.sync import sync_to_async as sta
from typing import (
    List,
    Any
)



def alist(args: List[Any]) -> List[Any]:
    return sta(list)(args)