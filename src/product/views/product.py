import imp
from itertools import product
from multiprocessing import context
from django.views import generic
from django.views.generic import ListView
from django.db.models import Q
from ..filters import ProductFilter
from product.models import Product
from django_filters.views import FilterView

class ProductListView(FilterView):
    model = Product
    paginate_by = 10 
    template_name='products/list.html'
    filterset_class = ProductFilter

      
    
    

    

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
