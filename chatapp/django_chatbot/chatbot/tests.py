from django.test import TestCase

# Create your tests here.
# Import necessary models
# from django.contrib.auth.models import User
from .models import Chat 

# Retrieve all entries in the Chat model
all_chats = Chat.objects.all()

for chat in all_chats:
    print(f"User: {chat.user.username}")
    print(f"Message: {chat.message}")
    print(f"Response: {chat.response}")
    print(f"Created At: {chat.created_at}")
    print("--------------")
