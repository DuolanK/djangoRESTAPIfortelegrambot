from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import MessageSerializer
from .models import Message
from rest_framework import generics


class MessageAPIList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class MessageAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
