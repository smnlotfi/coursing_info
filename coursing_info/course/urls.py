from django.urls import path
from .views import index,course

urlpatterns = [
    path('index',index,name='index'),
    path('<str:category>/<str:title>',course,name='course'),
]