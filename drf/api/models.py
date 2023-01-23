from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)


    def __str__(self):
        return self.text

