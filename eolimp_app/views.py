from django.shortcuts import redirect, render
from django.views.generic import ListView

from .models import *


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html')


def groups(request):
    return render(request, 'teacher_views/groups.html')


class GroupsListView(ListView):
    model = Group
    ordering = ('group_name', )
    context_object_name = 'groups'
    # template_name = 'teachers/task_change_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Group.objects.filter(teacher_id__user_id=user.pk)
        return queryset


class ProblemsListView(ListView):
    model = Problem
    ordering = ('date_created', )
    context_object_name = 'problems'
    # template_name = 'teachers/task_change_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Problem.objects.filter(teacher_id__user_id=user.pk)
        return queryset


class LecturesListView(ListView):
    model = Lecture
    ordering = ('date_created', )
    context_object_name = 'lectures'
    # template_name = 'teachers/task_change_list.html'

    def get_queryset(self):
        user = self.request.user
        queryset = Lecture.objects.filter(teacher_id__user_id=user.pk)
        return queryset
