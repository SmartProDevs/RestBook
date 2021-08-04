from rest_framework.viewsets import ModelViewSet
from .models import Author, Category, Book
from .serializers import AuthorSerializer, CategorySerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

# class AuthorViewSet(ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

class AuthorView(APIView):

    def get_object(self, pk):
        try:
            model = Author.objects.get(pk=pk)
        except Exception:
            raise NotFound("Author not found -----------")
        return model

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            author = self.get_object(kwargs.get("pk"))
            serializer = AuthorSerializer(author, many=False)
            return Response(serializer.data)
        else:
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        author = self.get_object(kwargs.get("pk"))
        serializer = AuthorSerializer(data=request.data, instance=author)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        author = self.get_object(kwargs.get("pk"))
        author.delete()
        return Response({"state": "deleted"})

class CategoryViewSet(APIView):

    def get_object(self, pk):
         try:
            model = Category.objects.get(pk=pk)
         except Exception:
            return NotFound("Ma'lumot mavjud emas")

         return model

    def get(self, request, *args, **kwargs):
         if kwargs.get("pk"):
            model = self.get_object(kwargs.get("pk"))
            serializer = CategorySerializer(model, many=False)
            return Response(serializer.data)
         else:
             model = Category.objects.all()
             serializer = CategorySerializer(model, many=True)
             return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = CategorySerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delete()
        return Response({"state":"deleted"})


class BookViewSet(APIView):
    def get_object(self, pk):
            try:
                model = Book.objects.get(pk=pk)
            except Exception:
                return NotFound("Ma'lumot mavjud emas")

            return model

    def get(self, request, *args, **kwargs):
            if kwargs.get("pk"):
                model = self.get_object(kwargs.get("pk"))
                serializer = BookSerializer(model, many=False)
                return Response(serializer.data)
            else:
                model = Book.objects.all()
                serializer = BookSerializer(model, many=True)
                return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        serializer = BookSerializer(data=request.data, instance=model)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        model = self.get_object(kwargs.get("pk"))
        model.delete()
        return Response({"state": "deleted"})
