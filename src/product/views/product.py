import imp
from django.views import generic
from django.views.generic import ListView

from product.models import Variant,Product


class ProductListView(ListView):
    model = Product
    paginate_by = 10 
    context_object_name = 'Product'
    template_name='products/list.html'

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
