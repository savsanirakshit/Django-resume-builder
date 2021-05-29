from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "Home"

urlpatterns = [
    path('', views.Home, name="Home"),
    path('index', views.Home, name="Home"),
    path('Resume', views.Resume, name="Resume"),
    path('Portfolio', views.Portfolio, name="Portfolio"),
    path('Contact', views.Contact, name="Contact"),
    path('Email', views.Email, name="Email"),
]


