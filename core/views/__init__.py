from dataclasses import fields
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core.models import Categoria, Editora, Livro, Autor
from core.serializers import CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer, AutorSerializer
from .autor import AutorViewSet
from .categoria import CategoriaViewSet
from .editora import EditoraViewSet
from .livro import LivroViewSet