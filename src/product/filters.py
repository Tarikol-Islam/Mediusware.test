from cgitb import lookup
from tkinter import Widget
import django_filters
from .models import Product, ProductVariant
from django import forms
class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    price_from = django_filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='lte')
    variant = django_filters.ModelChoiceFilter(field_name='productvariantprice__product_variant_two',  queryset=ProductVariant.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}) )

    class Meta:
        model = Product
        fields = ['title','price_from','price_to','variant']