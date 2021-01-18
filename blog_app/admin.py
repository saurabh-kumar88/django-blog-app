from django.contrib import admin
from .models import Post,Comment

"""
super user : 
sau88
Imgoingin@20
"""


class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'date_posted', 'author',)
  list_filter = ('date_posted',)
  search_fields = ('title',)



class CommentAdmin(admin.ModelAdmin):
  list_display = ('name', 'body', 'post', 'created_on', 'active')
  list_filter = ('active', 'created_on')
  search_fields = ('name', )
  actions = ['approve_comments']

  # def approve_comments(self, request, queryset):
  #   queryset.update(active=True)


# Register your models here.
admin.site.register( Comment, CommentAdmin )
admin.site.register( Post, PostAdmin )
