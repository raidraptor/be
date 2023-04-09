import sys

from fastapi import Depends
from schemas import PostCreate
import crud
from database import SessionLocal, engine
import praw
import models

models.Base.metadata.create_all(bind=engine)


reddit = praw.Reddit(
    client_id="qf7TJZrXXD-swdIOWC3sOA",
    client_secret="31u-0cqAENXkAC-uD5gtkkUy2sD5Dg",
    user_agent="testscript by u/prinzchiyo",
)

# print(reddit.user.me())


def crawlFunction(subreddit, number):
    for submission in reddit.subreddit(subreddit).top(limit=number):
        crud.create_post(SessionLocal(), PostCreate(name=submission.title,
                                                    text=submission.selftext, imgUrl=submission.url))
