from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import GenericAPIView


from .serializers import BlogSerializer
from .models import Blog

class BlogMixins(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    

class BlogMixins2(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    http_method_names = []

    