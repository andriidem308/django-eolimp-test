# import os
#
# from django.shortcuts import redirect, render
#
# from debugging.create_users import *
#
#
# def create_students(request):
#     module_dir = os.path.dirname(__file__)
#     file_path = os.path.join(module_dir, 'students')
#     data_file = open(file_path, 'r')
#     create_students_models(data_file)
#     return redirect('home')
#
#
# def create_teachers(request):
#     module_dir = os.path.dirname(__file__)
#     file_path = os.path.join(module_dir, 'teachers')
#     data_file = open(file_path, 'r')
#     create_teachers_models(data_file)
#     return redirect('home')
#
#
# def create_problems(request):
#     module_dir = os.path.dirname(__file__)
#     file_path = os.path.join(module_dir, 'problems')
#     data_file = open(file_path, 'r')
#     create_problems_models(data_file)
#     return redirect('home')
#
#
# def create_lectures(request):
#     module_dir = os.path.dirname(__file__)
#     file_path = os.path.join(module_dir, 'lectures')
#     data_file = open(file_path, 'r')
#     create_lectures_models(data_file)
#     return redirect('home')
