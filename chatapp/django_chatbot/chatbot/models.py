from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # session_id = models.CharField(max_length=100, default=' ') # Add this line

    def __str__(self):
        return f'{self.user.username}: {self.message}'


class Chatapp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat {self.pk}"

class Message(models.Model):
    class RoleChoices(models.TextChoices):
        USER = 'user'
        ASSISTANT = 'assistant'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    role = models.CharField(max_length=10, choices=RoleChoices.choices)
    timestamp = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chatapp, on_delete=models.CASCADE, related_name="messages")

    def __str__(self):
        return f"{self.role}: {self.content}"