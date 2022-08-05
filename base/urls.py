from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskEdit, TaskDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task-creat/', TaskCreate.as_view(), name='task_create'),
    path('task-edit/<int:pk>/', TaskEdit.as_view(), name='task_edit'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='task_list'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),


]
