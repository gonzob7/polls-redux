from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'registration'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
