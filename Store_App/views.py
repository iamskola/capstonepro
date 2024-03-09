from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer,ProductSerializer,CreateProductSerializer, UserCreateSerializer, StoreSerializer, CreateStoreSerializer
from rest_framework import status, exceptions, permissions
from django.contrib.auth. models import User
from .models import Category, Product, Store
from rest_framework import generics
#from .permission import IsStoreOwner
#from django.shortcuts import get_object_or_404

# Create your views here.

class CategoryEndpoint(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer


class SingleCategoryEndpoint(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'


class CategoryDeleteEndpoint(generics.DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'



class ProductEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        products=Product.objects.all()
        serializer=ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        serializer=CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ProductListEndpoint(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    def get_queryset(self):
        queryset=super().get_queryset()
        category=self.request.query_params.get('category')
        if category is not None:
            queryset=queryset.filter(category__name=category)
        return queryset
    

class ProductDetailEndpoint(APIView):
        def get_object(self, pk):
            try:
                product=Product.objects.get(id=pk)
                return product
            except Product.DoesNotExist:
                raise exceptions.NotFound(f'product with this id: {pk} does not exist')

        def get(self, request, *args, **kwargs):
            product=self.get_object(self.kwargs['product_id'])
            serializer=ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def put(self, request, *args, **kwargs):
            product=self.get_object(self.kwargs['product_id'])
            serializer=CreateProductSerializer(instance=product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


        def delete(self, request, *args, **kwargs):
            product=self.get_object(self.kwargs['product_id'])
            product.delete()
            return Response({'message':'product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)



class StoreEndpoint(generics.ListCreateAPIView):
     queryset=Store.objects.all()
     serializer_class=StoreSerializer
    
class StoreListEndpoint(generics.ListAPIView):
    serializer_class=StoreSerializer
    queryset=Store.objects.all()

    def get_queryset(self):
        queryset=super().get_queryset()
        store=self.request.query_params.get('store')
        if store is not None:
            queryset=queryset.filter(store__name=store)
        return queryset

class StoreDetailEndpoint(APIView):
        def get_object(self, pk):
            try:
                store=Store.objects.get(id=pk)
                return store
            except Store.DoesNotExist:
                raise exceptions.NotFound(f'store with this id: {pk} does not exist')

        def get(self, request, *args, **kwargs):
            store=self.get_object(self.kwargs['store_id'])
            serializer=StoreSerializer(store)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def put(self, request, *args, **kwargs):
            store=self.get_object(self.kwargs['store_id'])
            serializer=CreateStoreSerializer(instance=store, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


        def delete(self, request, *args, **kwargs):
            user=self.request.user
            store=self.get_object(self.kwargs['store_id'])
            store.delete()
            return Response({'message':'your store has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
