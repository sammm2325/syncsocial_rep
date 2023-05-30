from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class FreeDate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_friends')
    