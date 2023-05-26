from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.landing_page, name="landing"),
]
