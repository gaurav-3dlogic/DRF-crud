from rest_framework import viewsets
from my.models import studentform
from .serializers import studentserializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication

class crud(viewsets.ModelViewSet):
    queryset=studentform.objects.all()
    serializer_class=studentserializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]