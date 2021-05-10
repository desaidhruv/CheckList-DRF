from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)

from .permission import IsOwner

from .models import CheckList, CheckListItem

from .serializers import CheckListSerializer, CheckListItemSerializer

class CheckListsAPIView(ListCreateAPIView):
    """
    Listing and Creation
    """
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset

class CheckListAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy
    """
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset


class CheckListItemCreateAPIView(CreateAPIView):
    """
    Creation
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, Destroy
    """
    serializer_class = CheckListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user=self.request.user)
        return queryset
