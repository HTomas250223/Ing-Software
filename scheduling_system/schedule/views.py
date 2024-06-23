from rest_framework import viewsets
from .models import Aula, Docente, Horario
from .serializers import AulaSerializer, DocenteSerializer, HorarioSerializer
from .models import Horario
from .serializers import HorarioSerializer

class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    

# Create your views here.
