from django.urls import path
from .views import get_all_books,create_book,log_api
urlpatterns = [
    path('get_book/',get_all_books,name='get_book'),
    path('create_book/',create_book,name='create_book'),
    path('login_api/',log_api,name='login_api')
]