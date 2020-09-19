from django import forms
from blog_app.models import Comment 

class Search_Blog_Title(forms.Form):
  blog_query = forms.CharField(label='', required=True)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('body',)

class TestForm(forms.ModelForm):
  text = forms.CharField(label="type : 'yes or no'", required=True)
  class Meta:
    model = Comment
    fields = ('text',)


