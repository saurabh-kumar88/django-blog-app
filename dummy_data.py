import json
import random
import time
from blog_app.models import Post
# from django.contrib.auth.models import User

with open('posts.json') as f:
  posts_json = json.load(f)


for post in posts_json:
  post = Post(title=post['title'], content=post['content'], author_id="1")
  post.save()
  
  