from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, BookViewSet, AuthorView

# router = routers.DefaultRouter()
# router.register(r"authors", AuthorViewSet)
# router.register(r"categories", CategoryViewSet)
# router.register(r"books", BookViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    path('authors/', AuthorView.as_view(), name='authors-list'),
    path('authors/<int:pk>/detail', AuthorView.as_view(), name='authors-list'),

]