from pydantic import BaseModel


class PostBase(BaseModel):
    name: str
    text: str
    imgUrl: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int

    class Config:
        orm_mode = True
