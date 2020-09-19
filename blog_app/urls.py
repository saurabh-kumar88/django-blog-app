from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentEditView,
    CommentDeleteView,
    SearchBlogs,
) 
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('post/<int:pk>/comment/', views.post_detail, name='blog-detail'), # function based
    # path('post/<int:pk>/', PostDetailView.as_view(), name="blog-detail"),
    path('post/new/', PostCreateView.as_view(), name="blog-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="blog-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="blog-delete"),   
    path('about/', views.About, name='blog-about'),
    path('comment/<int:pk>/edit/', CommentEditView.as_view(), name="comment-edit"),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name="comment-delete"),
    path('search/', SearchBlogs.as_view(), name='search-blogs'),
   
    
    
 ]