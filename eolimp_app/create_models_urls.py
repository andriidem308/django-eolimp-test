from django.urls import include, path

from .create_models_views import *


urlpatterns = [
    path('students/', create_students, name='create_students'),
    path('teachers/', create_teachers, name='create_teachers'),
    path('problems/', create_problems, name='create_problems'),
    path('lectures/', create_lectures, name='create_lectures'),
]

