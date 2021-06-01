from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    first_name = models.CharField(max_length=200, blank=True) 
    last_name = models.CharField(max_length=200, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    bio = models.TextField(default="no bio...", max_length=300)
    email = models.EmailField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(default='avatar.png', upload_to='avatars/')
    friends = models.ManytoManyField(User, blank=True, related_name='friend')
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeFields(auto_now=True)
    created = models.DateTimeFields(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.created}"
