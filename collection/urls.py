from django.urls import path
from .views import get_all_collections 

urlpatterns = [
    path('user/<slug:username>', get_all_collections, name='all_collections'),
]