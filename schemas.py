from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    content: str | None = None


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Article] = []

    class Config:
        orm_mode = True
