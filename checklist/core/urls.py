from django.urls import path
from .views import (
    CheckListsAPIView,
    CheckListAPIView)

urlpatterns = [
    path('api/checklists/', CheckListsAPIView.as_view()),
    path('api/checklist/<int:pk>/', CheckListAPIView.as_view()),
]