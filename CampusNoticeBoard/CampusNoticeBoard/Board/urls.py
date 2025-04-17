from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentViewset, basename='students')
router.register('events', EventViewset, basename='events')
router.register('comments', CommentsViewset, basename='comments')
router.register('likes', LikeViewset, basename='likes')

urlpatterns = router.urls