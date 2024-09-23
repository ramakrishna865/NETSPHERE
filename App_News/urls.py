from django.urls import path
from . import views

app_name = 'App_News'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # path('<int:pk>/', views.article_detail, name='article_detail'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),

]
