from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .models import Product
from .serializers import ProductSerializer

class ProductList(APIView):
    def get(self, request):
        page = request.GET.get('page','1') # 페이지
        products_list = Product.objects.all()
        paginator = Paginator(products_list, 10)
        products = paginator.get_page(page)
        serializer = ProductSerializer(products.object_list, many=True)
        return Response({"전체상품 수" : paginator.count,
                        "전체 페이지" :  paginator.num_pages,
                        "현재 페이지" : products.number,
                        "목록":serializer.data})

    def post(self, request, *args, **kwargs):
        permission_classes = [IsAuthenticated]
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ProductDetail(APIView):
    def get_object(self, productid):
        return get_object_or_404(Product, pk=productid)

    def get(self, request, productid):
        product = self.get_object(productid)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, productid):
        # product = self.get_object(productid)
        # if product.author != request.user:
        #     return Response(status=status.HTTP_403_FORBIDDEN)
        # serializer = ProductSerializer(product, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(pk=productid)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, productid):
        product = self.get_object(productid)
        if product.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
