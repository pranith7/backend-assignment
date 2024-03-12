from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
import os,uuid
# Set environment variable for OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-xx"

from openai import OpenAI
client = OpenAI()

def ask_openai(message):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message}
    ]
    )

    answer = completion.choices[0].message.content.strip()
    return answer

# Create your views here.
def chatbot(request):
    # print(request.user.username)
    if not request.user.is_authenticated:
        return redirect('login')
    
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        chat_session_uuid = uuid.uuid4()  # Generate a UUID for the chat session

        response = ask_openai(message)
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})

def chat_session(request, session_id):
    chats = Chat.objects.filter(session_id=session_id)
    return render(request, 'chat_session.html', {'chats': chats, 'session_id': session_id})

def view_sessions(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Retrieve all unique session IDs for the current user
    sessions = Chat.objects.filter(user=request.user).values_list('session_id', flat=True).distinct()
    
    return render(request, 'view_sessions.html', {'sessions': sessions})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

