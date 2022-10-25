"""
Poly serializer.
"""
from typing import Optional

from pydantic import BaseModel


class PolySerializer(BaseModel):
    """
    Poly serializer.
    """
    name: str
    npinput: Optional[str]
    xsize: Optional[int]
    ysize: Optional[int]
    imagefile: Optional[str]
    arrayfile: Optional[str]
    exectime: Optional[float]

    class Config:
        """
        ORM mode.
        """
        orm_mode = True
