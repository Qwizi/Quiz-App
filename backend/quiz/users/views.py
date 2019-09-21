from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import UserSerializer, UserAnswerSerializer
from .models import User, UserAnswer

h201 = status.HTTP_201_CREATED
h400 = status.HTTP_400_BAD_REQUEST
h204 = status.HTTP_204_NO_CONTENT


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=h201)
        else:
            return Response(serializer.errors, status=h400)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=h204)


class UserQuizAnswerViewSet(viewsets.ViewSet):
    serializer_class = UserAnswerSerializer

    def create(self, request):
        request.data['user'] = self.kwargs['user_pk']
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=h201)
        else:
            return Response(serializer.data, status=h400)
