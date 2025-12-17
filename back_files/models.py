from sqlmodel import SQLModel, Field
from typing import Optional

class Brainrot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    score: int