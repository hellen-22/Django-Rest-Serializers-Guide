from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import api_view
from rest_framework import status


from .serializers import *
from .models import *
# Create your views here.

"""CLASS BASED API VIEW"""
class BlogCreateGetApiView(APIView):
    def post(self, request, format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

class BlogRetrieveUpdateDeleteApiView(APIView):
    def get(self, request, pk, format=None):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          

"""USE OF MIXINS"""
class BlogMixins(CreateModelMixin, 
                            ListModelMixin, 
                            RetrieveModelMixin, 
                            UpdateModelMixin, 
                            DestroyModelMixin, 
                            GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogMixins2(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


"""Using Generic Api Views"""
class BlogListCreateGenericApi(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
  
class BlogRetrieveUpdateDestroyGenericApi(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


"""FUNCTION BASED VIEWS"""
@api_view(['GET','POST'])
def blog_list_create(request):
    if request.method == 'GET':
        blog = Blog.objects.all()
        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
  
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET','PUT','PATCH','DELETE'])
def blog_retrieve_update_delete(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
  
    elif request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'PATCH':
        serializer = BlogSerializer(blog, data=request.data, partial=True)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)