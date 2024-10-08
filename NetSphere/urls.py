from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('blog/', include('App_Blog.urls')),
    path('', views.index, name='index'),
    path('news/', include('App_News.urls')),
    path('community/', include('App_DC.urls',namespace='App_DC')),


]
# blog/details/(?P<slug>[-a-zA-Z0-9_/()]+)$


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
