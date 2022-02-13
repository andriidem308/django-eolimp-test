from django.contrib.auth import views as auth_views
from django.urls import include, path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', auth_views.LoginView.as_view(
        template_name="pre_login.html", redirect_authenticated_user=True), name='login'
         ),
    path('logout/', auth_views.LogoutView.as_view(template_name='pre_login.html'), name='logout'),

    path('groups/', GroupsListView.as_view(template_name='teacher_views/groups_list.html'), name='groups'),
    path('problems/', ProblemsListView.as_view(template_name='teacher_views/problems_list.html'), name='problems'),
    path('lectures/', LecturesListView.as_view(template_name='teacher_views/lectures_list.html'), name='lectures'),

]

