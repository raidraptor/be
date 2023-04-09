from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    text: Mapped[Optional[str]]
    imgUrl: Mapped[Optional[str]]
    # comments: Mapped[List["Comment"]] = relationship(
    #     back_populates="post", cascade="all, delete-orphan"
    # )

    def __repr__(self) -> str:
        return f"Post(id={self.id!r}, name={self.name!r}, fullname={self.text!r})"


# class Comment(Base):
#     __tablename__ = "comment"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     text: Mapped[Optional[str]]
#     post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
#     post: Mapped["Post"] = relationship(back_populates="comments")

#     def __repr__(self) -> str:
#         return f"Comment(id={self.id!r}, text={self.text!r})"
