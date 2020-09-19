from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog_app.models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView, 
    )
from blog_app.forms import Search_Blog_Title, CommentForm
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
  model = Post
  template_name = 'blog_app/home.html' #<app name>/<model>_<viewtype>.html
  context_object_name = 'posts'
  ordering = ['-date_posted']
  paginate_by = 5
  
class UserPostListView(ListView):
  model = Post
  template_name = 'blog_app/user_posts.html' #<app name>/<model>_<viewtype>.html
  context_object_name = 'posts'
  paginate_by = 5

  def get_queryset(self):
    user = get_object_or_404(User, username=self.kwargs.get('username'))
    return Post.objects.filter(author=user).order_by('-date_posted')
class PostDetailView(DetailView):
  model = Post
 
class PostCreateView( LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user # before submitting the form, take form instance.author and assign it to current logged-in user
    return super().form_valid(form) # form validation on parent class 

class PostUpdateView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
  model = Post
  fields = ['title', 'content']

  def form_valid(self, form):
    form.instance.author = self.request.user 
    return super().form_valid(form)
  
  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

class PostDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Post
  success_url = '/'

  def test_func(self):
    post = self.get_object()
    if self.request.user == post.author:
      return True
    return False

def post_detail(request, pk):
  template_name = 'blog_app/post_detail.html'
  post = get_object_or_404(Post, pk=pk)
  comments = post.comments.filter(active=True)
  new_comment = None
  # Comment posted
  if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
      comment_form.instance.name = request.user
      # Create Comment object but don't save to database yet
      new_comment = comment_form.save(commit=False)
      # Assign the current post to the comment
      new_comment.post = post
      # Save the comment to the database
      new_comment.save()
      return redirect('blog-detail', pk=post.pk)
  else:
    comment_form = CommentForm()

  return render(request, 
                template_name, 
                  {
                  'post': post,
                  'comments': comments,
                  'new_comment': new_comment,
                  'comment_form': comment_form,
                  'User' : str(request.user),
                  }
                )
                
class CommentEditView( LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
  model = Comment
  fields = ['body',]
  
  def form_valid(self, form):
    form.instance.name = str(self.request.user) 
    return super().form_valid(form)
  
  def test_func(self):
    comment = self.get_object()
    if str(self.request.user) == comment.name:
      return True
    return False
  
  def get_success_url(self):
      comment = self.get_object() 
      return reverse_lazy( 'blog-detail', kwargs={'pk': comment.post.pk })
  
  
class CommentDeleteView( LoginRequiredMixin, UserPassesTestMixin, DeleteView):
  model = Comment
  
  def test_func(self):
    comment = self.get_object()
    if str(self.request.user) == comment.name:
      return True
    return False

  def get_success_url(self):
      comment = self.get_object() 
      return reverse_lazy( 'blog-detail', kwargs={'pk': comment.post.pk })


class SearchBlogs(ListView):
  model = Post
  template_name = 'blog_app/search_results.html'
  
  def get_queryset(self):
    query = self.request.GET.get('search_query')
    return Post.objects.filter(title__icontains=query) 


def search_blogs(request):
  
  if request.method == 'POST':
    blog_title = request.POST.get('blogs_requested')
    posts = Post.objects.all().filter(title=blog_title)
    if posts:
      context = {
        'posts': posts,
      }
      return render(request, 'blog_app/requested_blogs.html', context )
    else:
      msg = "No Such Post Found!"
  return render(request, 'blog_app/requested_blogs.html', {'msg' : msg} )


def About(request):
  return render(request, "blog_app/about.html", {"message" : "About page working Ok."})