from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register-store/', views.register_store, name='register_store')
]
