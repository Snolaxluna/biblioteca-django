from rest_framework import generics

from core.filters import LivroFilter
from .models import Livro
from .serializers import LivroSerializer


class LivroList(generics.ListCreateAPIView): # type: ignore
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-list"


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"

class LivroList(generics.ListAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    filterset_class = LivroFilter
    ordering_fields = ['titulo', 'autor__nome', 'categoria__nome', 'publicado_em']
    ordering = ['titulo']