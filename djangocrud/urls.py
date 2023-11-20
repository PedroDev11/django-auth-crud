from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.signout, name="logout"),
    
    path('tasks/', views.tasks, name="tasks"),
    path('completed-tasks/', views.tasksCompleted, name="completed-tasks"),
    path('detail-task/<int:task_id>', views.taskDetail, name="detail-task"),
    path('detail-task/<int:task_id>/complete', views.taskComplete, name="complete-task"),
    path('detail-task/<int:task_id>/delete', views.taskDelete, name="delete-task"),
    path('create-task/', views.taskCreate, name="create-task")
]
