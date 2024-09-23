# user_app/urls.py

from django.urls import path
from .views import UserDetailsView

urlpatterns = [
    path('users/', UserDetailsView.as_view(), name='user-details-list'),
]
