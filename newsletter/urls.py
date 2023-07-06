from django.urls import path
from newsletter import views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('confirm-email/<slug:confirmation_id>', views.confirmation, name='confirm_newsletter_email'),
]
