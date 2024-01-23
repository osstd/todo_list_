from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, CustomDeleteView, CustomLoginView, RegisterPage

from django.contrib.auth.views import LogoutView

# url resolver can't use the class, so we trigger a method that TaskList(ListView) has .as_view
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', CustomDeleteView.as_view(), name='task-delete')
]
