from django.urls import path
from .views import user, issue_token, user_info

urlpatterns = [
    path('user/', user, name='user'),
    path('user/<slug:username>/', user_info, name='user_info'),
    path('login/', issue_token, name='issue_token'),
]