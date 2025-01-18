from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('detect-intent/', views.detect_intent, name='detect_intent'),
]
