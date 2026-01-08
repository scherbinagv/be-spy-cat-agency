from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SpyCat
from .serializers import SpyCatSerializer

class SpyCatViewSet(ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer
    http_method_names = ["get", "post", "delete", "patch"]
