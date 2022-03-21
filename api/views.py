from rest_framework import generics
from events import models
from .serializers import EventSerializer

class ListEvent(generics.ListCreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = EventSerializer


class DetailEvent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = EventSerializer
