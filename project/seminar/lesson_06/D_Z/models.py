from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str = Field()
    description: str | None = Field(default=None)
    done: bool = Field(default=False)


class TaskOut(TaskIn):
    id: int
