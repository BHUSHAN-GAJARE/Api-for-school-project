from django.shortcuts import render
from .serializers import StudentSerializers
from.models import Student
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class StudentRegi(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializers

    authenticaltion_classes=[JWTAuthentication]
    perimission_classes=[DjangoModelPermissions]

