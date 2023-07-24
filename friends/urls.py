from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('friend', views.FriendViewSet, 'friend')

urlpatterns = [
      path('', include(router.urls)),
      path('search/', views.FriendsSearchList.as_view(), name='search'),
]
