from django.db import models

#Basic User Model
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos') #mandatory
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png') #optional field
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #metaclass
    class Meta:
        #- decending ordring, + acending ordering
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])