import random

from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
)
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Product, User
from .serializers import ProductSerializer


class ProductViewSet(ViewSet):
    def list(self, request: Request) -> Response:
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def create(self, request: Request) -> Response:
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def retrieve(self, request: Request, pk: str) -> Response:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request: Request, pk: str) -> Response:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_202_ACCEPTED)

    def destroy(self, request: Request, pk: str) -> Response:
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class UserAPIView(APIView):
    def get(self, _: None) -> Response:
        users = User.objects.all()
        user = random.choice(users)
        return Response({"id": user.pk})
