from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('friend', views.FriendViewSet, 'friend')
#router.register('friend/usersearch', views.FriendProfileViewSet, 'usersearch')

urlpatterns = [
      path('', include(router.urls)),
]
