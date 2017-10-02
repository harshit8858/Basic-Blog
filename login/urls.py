from django.conf.urls import url
from django.contrib import admin
from lapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index, name='index'),     # dollar sign represent that this regular expression is done, it is not neccessary to put a dollar sign.
    url(r'^$', homepage, name='homepage'),     # if no $ sign....then 8000/profile and 8000/profile/jkdfhjkdhfjkdf means the same
    url(r'^login/$', login, name='login'),
    url(r'^auth_check/$', auth_check, name='check'),
    url(r'^register/$', register, name='register'),
    url(r'^invalid/$', invalid),
    url(r'^logout/$',logout, name='logout'),
    url(r'^delete/(\d+)$', delete, name='delete'),
    url(r'^network/delete/(\d+)$', delete, name='delete'),
    url(r'^search/$', search),
    url(r'^edit/(\d+)/$', edit, name="edit"),
    url(r'^profile/$', profile, name='profile'),
    url(r'^my_files/$', my_files, name='my_files'),
    url(r'^profile1/(\d+)/$', profile1, name='profile1'),
    url(r'^home/$', home, name='home'),
    url(r'^network/$', network, name='network'),
    url(r'^cpassword/$', password, name='cpassword'),
    url(r'^comment/$', comment, name='comment'),
    url(r'^network/ajax_sample/$', ajax_sample, name='ajax_sample'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)