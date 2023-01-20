
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


from .serializers import MessageSerializer
from .models import Message
from rest_framework import generics

class MessageAPIView(APIView):
    def get(self, request):
        q = Message.objects.filter(user=request.user)
        return Response({'posts': MessageSerializer(q, many=True).data})
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': serializer.data})
        else:
            return Response.status_code(500)

class MessageAPIList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get(self, request):
        q = Message.objects.filter(user=request.user)
        return Response({'posts': MessageSerializer(q, many=True).data})

class MessageAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
