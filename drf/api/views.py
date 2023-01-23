
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


from .serializers import MessageSerializer, MessageSerializerRead
from .models import Message
from rest_framework import generics
import secrets


class MessageAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        q = Message.objects.filter(user=request.user)
        return Response({'posts': MessageSerializer(q, many=True).data})


class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializerRead
    permission_classes = (IsAuthenticatedOrReadOnly,)

class MessageAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

def generate_token(request):

    message = Message.objects.filter(user=request.user)
    for i in message:
        i.token = secrets.token_hex(16)
        i.save()
    return render(request, 'api/generate_token.html', {'message': message})