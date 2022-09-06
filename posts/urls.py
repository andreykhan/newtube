from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('group/<slug:name>/', group_posts),
]
