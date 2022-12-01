from dataclasses import fields
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Categoria, Editora, Livro, Autor
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer, AutorSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return LivroDetailSerializer
        return LivroSerializer