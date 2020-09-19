from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

"""
redirect() --> redirects control to a specific route
reverse() --> return the full url to that route as a string
"""

class Post(models.Model):
  """Post model : 
  one--> many relation (a user can have multiple post but every post can have only one author)
  on_delete=models.CASCADE, this argument tells delete the post if its author get deleted (reverse is not possible)
  """
  title = models.CharField(max_length=100)
  content = models.TextField() # unrestricted lines of text
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)   
  # '__' --> dunder function i.e double underscore
  def __str__(self): 
    return self.title
  
  def get_absolute_url(self):
    return reverse('blog-detail', kwargs={'pk' : self.pk})

class Comment(models.Model):
  post = models.ForeignKey('blog_app.Post', on_delete=models.CASCADE, related_name='comments')
  name = models.CharField(max_length=200)
  body = models.TextField()
  created_on = models.DateTimeField(default=timezone.now)
  active = models.BooleanField(default=True)
  
  class Meta:
    ordering = ['created_on',]

  def __str__(self):
    return self.body  


