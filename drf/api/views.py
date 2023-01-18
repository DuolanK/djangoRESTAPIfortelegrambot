from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class NoteAPIList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteAPIView(APIView):
    def get(self, request):
        n = Note.objects.all()
        return Response({'title': NoteSerializer(n, many=True).data})

    def post(self,request):
        serializer = NoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        try:
            instance = Note.objects.get(pk=pk)
        except:
            return Response({"error": "Object doesnt exist"})

        serializer = NoteSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})
        try:
            post = Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Response({"error": "Post not found"})
        post.delete()
        return Response({"message": "Post deleted successfully"})
#class NoteAPIView(generics.ListAPIView):
#    queryset = Note.objects.all()
#   serializer_class = NoteSerializer
