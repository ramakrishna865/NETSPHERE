from django.contrib import admin
from django.urls import path
from App_DC.views import *
 

app_name='App_DC'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
]