import sys
import models
from database import engine
import praw


# models.Base.metadata.create_all(bind=engine)
reddit = praw.Reddit(
    client_id="qf7TJZrXXD-swdIOWC3sOA",
    client_secret="31u-0cqAENXkAC-uD5gtkkUy2sD5Dg",
    user_agent="testscript by u/prinzchiyo",
)

# print(reddit.user.me())
for submission in reddit.subreddit(sys.argv[1]).hot(limit=3):
    print(submission.title)
    print(submission.selftext)
    print(submission.url)
