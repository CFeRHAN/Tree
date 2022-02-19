from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', null=True)
    bio = models.CharField(max_length=1000, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class FollowersCount(models.Model):
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Insight(models.Model):
    user = models.ForeignKey(User, related_name='Insight', on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    body = models.TextField()
    