from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, register, login

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', register, name='register'),
    path('auth/login/', login, name='login'),
]