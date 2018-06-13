from django.contrib import admin
from .models import *
from django.contrib.sessions.models import Session

admin.site.register(Box)
admin.site.register(Session)
admin.site.register(Comment)
admin.site.register(Profile_pic)
