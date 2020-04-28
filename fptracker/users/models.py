from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    history_text = models.CharField(max_length = 100, null = True, blank = True)
    favorite_text = models.CharField(max_length = 100, null = True, blank = True)
