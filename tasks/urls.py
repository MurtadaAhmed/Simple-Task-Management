from django.core.management.commands.runserver import naiveip_re
from django.urls import path

from . import views

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
