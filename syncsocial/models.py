from django.db import models
from django.contrib.auth.models import User

class FreeDate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='free_dates')
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_friends')
    