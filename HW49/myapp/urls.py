from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserListView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('api/users/', UserListView.as_view(), name='user-list'),
]