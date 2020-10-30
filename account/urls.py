from django.urls import path
from account import views

app_name = 'sign'


urlpatterns = [
    path('', views.signupview, name='signup'),
    path('con/', views.confirm, name='con'),
]