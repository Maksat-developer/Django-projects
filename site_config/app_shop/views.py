from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProductSerializers, CategorySerializers
from .models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filterset_fields = ['name']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


# class SubCategoryViewSet(viewsets.ModelViewSet):
#     queryset = SubCategory.objects.all()
#     serializer_class = SubCategoruSerializers
