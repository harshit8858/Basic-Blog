from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Box(models.Model):
    username = models.ForeignKey(User,blank=True,null=True)
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now=True,blank=True,null=True)
    pic = models.FileField(upload_to='images',blank=True, null=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']


class Profile(models.Model):
    user = models.OneToOneField(User)
    job = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    profile_pic = models.FileField(upload_to='images',blank=True,null=True)
    number = models.IntegerField()

    class Meta:
        db_table = 'auth_profile'

    def __str__(self):
        return self.job

# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# def save_user_profile(sender,instance,**kwargs):
#     instance.profile.save()
#
# post_save.connect(create_user_profile, sender=User)
# post_save.connect(save_user_profile, sender=User)

class Comment(models.Model):
    user = models.ForeignKey(User, blank=True,null=True)
    box = models.ForeignKey(Box, blank=True,null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.comment

class like(models.Model):
    count =models.CharField(max_length=20,default="no")

    def __str__(self):
        return self.count

class Commnet2(models.Model):
    class Meta:
        db_table = 'django_comments'
