from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa
    path('', views.blog_list, name='blog_list'),  # Blog listesi
    path('insankaynaklari/<slug:slug>/', views.blog_detail, name='blog_detail'),  # Blog detay
]