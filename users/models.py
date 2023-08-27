from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default='profile.jpg' , upload_to='profile_pic')
    contact_number = models.CharField(max_length=20 , default=+123456789)
    def __str__(self) -> str:
        return self.user.username