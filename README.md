# be


ask to crawl posts:
curl -X 'POST' \
  'http://127.0.0.1:8000/crawl/?subreddit=personalfinance&number=10' \
  -H 'accept: application/json' \
  -d ''

get list of posts:
curl -X 'GET' \
  'http://127.0.0.1:8000/posts/' \
  -H 'accept: application/json'
  
