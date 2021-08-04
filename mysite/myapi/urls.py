from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r"authors", AuthorViewSet)
# router.register(r"categories", CategoryViewSet)
# router.register(r"books", BookViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    path('authors/', AuthorView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', AuthorView.as_view(), name='authors-list'),

    path('categories/', CategoryView.as_view(), name='categories-list'),
    path('categories/<int:pk>/', CategoryView.as_view(), name='categories-list'),

    path('books/', BookView.as_view(), name='books-list'),
    path('books/<int:pk>/', BookView.as_view(), name='books-list'),

]