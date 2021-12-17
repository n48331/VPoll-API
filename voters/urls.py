from django.urls import path
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('voters-list/', VotersListView.as_view()),
    path('voters-details/<int:pk>/', VotersView.as_view()),
]
