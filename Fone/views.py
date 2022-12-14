from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import FoneSerializer, CircuitSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
from .models import Fone, Circuits
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class FoneListView(ListCreateAPIView):
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer


class FoneDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CircuitsListView(ListCreateAPIView):
    queryset = Circuits.objects.all()
    serializer_class = CircuitSerializer
    permission_classes = [AllowAny]


class CircuitsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Circuits.objects.all()
    serializer_class = CircuitSerializer
    permission_classes = [AllowAny]
