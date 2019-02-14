from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Stores
from django.core.paginator import Paginator

# Create your views here.
def listing(request):
    stores_list = Stores.objects.all().order_by('storeid')
    paginator = Paginator(stores_list, 8)
    page = request.GET.get('page', 1)
    stores = paginator.get_page(page)
    return render(request, 'kfcstores/index.html', {'stores': stores})

class StoresDetailView(generic.DetailView):
    model = Stores
    template_name = 'kfcstores/detail.html'
    context_object_name = 'store'
