from pydantic import BaseModel


class Movie(BaseModel):
    id: int
    title: str
    description: str | None = None
    genre: str


class Song(BaseModel):
    id: int
    name: str
    author: str
    description: str | None = None
    genre: str
