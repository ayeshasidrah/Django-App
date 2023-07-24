from django.db import models


class FriendsProfile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
