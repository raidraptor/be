from sqlalchemy.orm import Session

import models
import schemas


def get_posts(db: Session):
    return db.query(models.Post).all()


def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(
        name=post.name, text=post.text, imgUrl=post.imgUrl)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
