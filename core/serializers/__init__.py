from rest_framework.serializers import ModelSerializer

from core.models import Autor, Categoria, Editora, Livro

from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .livro import LivroDetailSerializer, LivroSerializer