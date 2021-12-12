from django.urls import path
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('voters-list/', VoterView.as_view()),
]
