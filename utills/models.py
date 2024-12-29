from typing import Dict
from pydantic import BaseModel


class _Display(BaseModel):
    height: float
    width: float


class Settings(BaseModel):
    display: _Display | None = None

