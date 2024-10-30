from django.urls import path 
from core.views import Core

urlpatterns = [
    path('', Core, name='core'),
]