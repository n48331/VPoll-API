from django.urls import path
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('register/', RegisterView.as_view()),
]
