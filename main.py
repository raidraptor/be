from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from crawl import crawlFunction

import crud
import models
import schemas
from database import SessionLocal, engine


app = FastAPI()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/posts/", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(get_db)):
    posts = crud.get_posts(db)
    return posts


@app.post("/crawl/")
def crawl(subreddit: str, number: int):
    crawlFunction(subreddit=subreddit, number=number)
