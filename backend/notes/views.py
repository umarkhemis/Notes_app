from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializer import UserSerializer, NotesSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Notes

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class NotesView(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)
    
    
    def perform_create(self, serializer):
        if serializer.is_valid:
            serializer.save(author=self.request.user)
        else:
            print(serializer.error)
            

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NotesSerializer
    pagination_class = [IsAuthenticated]
    
    def get_queryset(self):
        return Notes.objects.filter(author=self.request.user)