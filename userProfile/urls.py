from django.urls import path
from .views import user, issue_token, user_info, user_register, user_update

urlpatterns = [
    path('user/', user, name='user'),
    path('user/update/', user_update, name='user_update'),
    path('user/<slug:username>/', user_info, name='user_info'),
    path('login/', issue_token, name='issue_token'),
    path('register/', user_register, name='register'),
]