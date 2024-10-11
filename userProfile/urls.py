from django.urls import path
from .views import ProfileView, user, issue_token

urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path('user/', user, name='user'),
    path('login/', issue_token, name='issue_token'),
]