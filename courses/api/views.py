from rest_framework import generics
from rest_framework.serializers import Serializer
from ..models import Subject
from .serializers import SubjectSerializer

class SubjectListView(generics.ListAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer