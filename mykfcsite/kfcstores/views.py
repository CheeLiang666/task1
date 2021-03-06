from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from .models import Stores
from django.core.paginator import Paginator

# Create your views here.
def listing(request):
    stores_list = Stores.objects.all().order_by('storeid')
    paginator = Paginator(stores_list, 4)
    page = request.GET.get('page', 1)
    stores = paginator.get_page(page)
    return render(request, 'kfcstores/index.html', {'stores': stores})

def getKFCsLatLng(request):
    stores_list = Stores.objects.all()
    jsonLocationData = []
    for store in stores_list:
        locationDict = {'id': store.storeid, 'name': store.storename, 'address': store.storeaddress, 
        'phone': store.storephone, 'latitude': store.latitude, 'longitude': store.longitude,
        'weekdayopen': store.weekdayopen, 'weekdayclose': store.weekdayclose, 
        'weekendopen': store.weekendopen, 'weekendclose': store.weekendclose}
        jsonLocationData.append(locationDict)
    return JsonResponse({"data": jsonLocationData})

def drawKFCMap(request):
    return render(request, 'kfcstores/map.html')

class StoresDetailView(generic.DetailView):
    model = Stores
    template_name = 'kfcstores/detail.html'
    context_object_name = 'store'
