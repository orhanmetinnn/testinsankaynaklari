from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insankaynaklari/<slug:slug>/', views.blog_detail, name='blog_detail'),
]
