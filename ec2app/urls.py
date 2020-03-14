from django.urls import path
from .views import m1
urlpatterns = [
    path('',m1,name="m1")]