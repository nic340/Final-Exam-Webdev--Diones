from sqlmodel import SQLModel, Field

class Brainrot(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    image: str
    user_id: int

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str