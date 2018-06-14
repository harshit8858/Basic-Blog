from django.db import models
from django.contrib.auth.models import User


class Box(models.Model):
    username = models.ForeignKey(User,blank=True,null=True)
    title = models.CharField(max_length=1000)
    content = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now=True,blank=True,null=True)
    image = models.FileField(upload_to='images/',blank=True, null=True)
    url = models.URLField()
    like = models.IntegerField(default=0)
    dis = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-like']


class Comment(models.Model):
    user = models.ForeignKey(User, blank=True,null=True)
    box = models.ForeignKey(Box, blank=True,null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.comment


class Profile_pic(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    p_pic = models.FileField(upload_to="profile_pic/", blank=True, null=True)

    def __str__(self):
        return str(self.user)