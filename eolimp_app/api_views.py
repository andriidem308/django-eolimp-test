from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
# from rest_framework.views import APIView

from .serializers import *


class TeacherRetrieveView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherUpdateView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = CreateTeacherSerializer


class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = CreateTeacherSerializer


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# class TeacherListView(APIView):
#     def get(self, request):
#         queryset = Teacher.objects.all()
#         serializer_class = TeacherSerializer(queryset, many=True)
#
#         return Response({'teachers:', serializer_class.data})


class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer


class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer


class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Create your views here.
