from django.urls import path
from . import views

app_name = 'navigation'
urlpatterns = [
    path('last_points', views.last_points, name='last_points')
]
