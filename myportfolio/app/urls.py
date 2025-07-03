from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # Add other app-specific paths here
    # path("about/", views.about, name="about"),
    # path("contact/", views.contact, name="contact"),
]
