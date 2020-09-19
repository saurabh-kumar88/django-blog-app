from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# from PIL import Image
# Create your models here.

class Profile(models.Model):
  """
  # one to one relation between User and Profile (one user can have one profile only)
  # on_delete=models.CASCADE is a one way operation (delete profile if user get deleted, reverse is not possible)
  """
  user = models.OneToOneField(User, on_delete=models.CASCADE )
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')  
  
  def __str__(self):
    return f'{self.user.username} Profile'



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
  instance.profile.save()
  