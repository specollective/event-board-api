from django.urls import path
from .views import ListEvent, DetailEvent

urlpatterns = [
    path('', ListEvent.as_view()),
    path('<int:pk>/', DetailEvent.as_view()),
]
