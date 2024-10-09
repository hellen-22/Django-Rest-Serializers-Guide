from django.urls import path, include
from .fbv import blog_list_create, blog_retrieve_update_delete
from .apiview import BlogCreateListApiView, BlogRetrieveUpdateDeleteApiView
from .generics import BlogListCreateGenericApi, BlogRetrieveUpdateDestroyGenericApi
from .mixin import BlogMixins, BlogMixins2

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("blog-mixins", BlogMixins, basename="blog-mixins")
router.register("blog-mixins2", BlogMixins2, basename="blog-mixins2")

urlpatterns = [
    # Function based views url patterns
    path("blog/", blog_list_create, name="blog"),
    path("blog/<int:pk>/", blog_retrieve_update_delete, name="blog-1"),

    # api view
    path("blog-api-view/", BlogCreateListApiView.as_view(), name="blog-api-view"),
    path("blog-api-view/<int:pk>/", BlogRetrieveUpdateDeleteApiView.as_view(), name="blog-api-view-1"),

    path("blog-generic-api/", BlogListCreateGenericApi.as_view(), name="blog-generic-api"),
    path("blog-generic-api/<int:pk>/", BlogRetrieveUpdateDestroyGenericApi.as_view(), name="blog-generic-api-1"),

    path("", include(router.urls))
]
