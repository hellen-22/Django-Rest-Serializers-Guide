from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


from .serializers import BlogSerializer
from .models import Blog

class BlogListCreateGenericApi(ListCreateAPIView):
    queryset = Blog.objects.all()

    def get_serializer_class(self):
        if self.method == 'POST':
            return BlogSerializer
        

  
class BlogRetrieveUpdateDestroyGenericApi(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer