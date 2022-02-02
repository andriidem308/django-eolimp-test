from django.urls import include, path

from .api_views import *


urlpatterns = [
    path('teachers/<int:pk>', TeacherRetrieveView.as_view()),
    path('teachers/update/<int:pk>', TeacherUpdateView.as_view()),
    path('teachers/all/', TeacherListView.as_view()),
    path('teachers/new', TeacherCreateView.as_view()),

    path('students/<int:pk>', StudentRetrieveView.as_view()),
    path('students/update/<int:pk>', StudentUpdateView.as_view()),
    path('students/all/', StudentListView.as_view()),
    path('students/new', StudentCreateView.as_view()),

]

