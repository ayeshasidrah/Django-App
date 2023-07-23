from django.db import models
from friendship.models import FriendshipManager


class FriendsProfile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)

   # objects = FriendshipManager()
