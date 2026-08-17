from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from StudentApp.models import Student
from .serializers import StudentSerializer


class StudentListCreateView(
    generics.ListCreateAPIView
):
    queryset = Student.objects.all()

    serializer_class = StudentSerializer

    authentication_classes = [
        BasicAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]


class StudentDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = Student.objects.all()

    serializer_class = StudentSerializer

    authentication_classes = [
        BasicAuthentication
    ]

    permission_classes = [
        IsAuthenticated
    ]


from django.shortcuts import render

# Create your views here.
