from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom, UserUpdateForm, ProfileUpdateForm 




# Create your views here.

def register(request):
  if request.method == 'POST':
    form = UserRegisterFrom(request.POST)
    if form.is_valid():
      form.save()
      userName = form.cleaned_data.get('username')
      messages.success(request, f'Account have been created for user name {userName}. You can now login.')
      return redirect('user-login')
  else:
    form = UserRegisterFrom()  
  return render(request, 'user/register.html', {'form' : form})


@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,
                               request.FILES,
                               instance=request.user.profile)
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      messages.success(request, f'Your profile have been updated')
      return redirect('user-profile')

  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

  context = {
    'u_form' : u_form,  
    'p_form' : p_form,
  }
  return render(request, 'user/profile.html', context)
 
