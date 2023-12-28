from django.urls import path
from .views import hellodjango

urlpatterns=[
    path('home/',hellodjango,name='home')
]