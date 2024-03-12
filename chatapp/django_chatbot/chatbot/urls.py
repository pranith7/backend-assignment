from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('chats/<str:session_id>/', views.chat_session, name='chat_session'),
    path('view_sessions/', views.view_sessions, name='view_sessions'),
]