from typing import Annotated
from pydantic import Field


IdField = Annotated[int, Field(gt = 0 )]
ShortTextField = Annotated[str, Field(min_length=1, max_length=128)]
LongTextField = Annotated[str, Field(min_length=1, max_length=1028)]
