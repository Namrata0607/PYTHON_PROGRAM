from django.urls import path
from . import views

urlpatterns = [
    path('', views.hobbies_view, name='hobbies'),  # Home page for hobbies
]
