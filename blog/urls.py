from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("blog-mixins", views.BlogMixins, basename="blog-mixins")
router.register("blog-mixins2", views.BlogMixins2, basename="blog-mixins2")

urlpatterns = [
    path("blog-api-view/", views.BlogCreateGetApiView.as_view(), name="blog-api-view"),
    path("blog-api-view/<int:pk>/", views.BlogRetrieveUpdateDeleteApiView.as_view(), name="blog-api-view-1"),

    path("blog-generic-api/", views.BlogCreateGetApiView.as_view(), name="blog-generic-api"),
    path("blog-generic-api/<int:pk>/", views.BlogRetrieveUpdateDestroyGenericApi.as_view(), name="blog-generic-api-1"),

    path("blog/", views.blog_list_create, name="blog"),
    path("blog/<int:pk>/", views.blog_retrieve_update_delete, name="blog-1"),


    path("blog-mixin", include(router.urls))
]
