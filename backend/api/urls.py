from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiCommands, name="api-cmds"),
    path('task-list/', views.taskList, name="task-list"),
    path('task/<str:id>/', views.getTask, name="get-task"),
    path('add-task/', views.addTask, name="add-task"),
    path('change-status/<str:id>/', views.changeStatus, name="change-task"),
    path('remove-task/<str:id>/',views.removeTask, name="remove-task"),
    path('modify/',views.modifyTask,name="modify-task")
]

#127.0.0.1:8000/api/task/2/