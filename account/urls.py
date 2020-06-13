from django.urls import path

from . import views


urlpatterns = [
    path('registro/', views.SignUp.as_view(), name='signup'),
]