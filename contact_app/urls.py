from django.urls import path

from .views import ContactUsView

urlpatterns = [path("contact/", ContactUsView.as_view(), name="public_contact")]