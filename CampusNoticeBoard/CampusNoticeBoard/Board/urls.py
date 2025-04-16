from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostViewset, basename='post')

urlpatterns = router.urls