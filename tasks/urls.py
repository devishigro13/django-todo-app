
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),

    # Task pages
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/completed/', views.completed_tasks, name='completed_tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('tasks/edit/<int:id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:id>/', views.delete_task, name='delete_task'),
    path('tasks/toggle/<int:id>/', views.toggle_task_status, name='toggle_task_status'),

    # Authentication
    path('signup/', views.signup, name='signup'),
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]
