from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from .models import Stores
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request, 'StoreTinder/index.html')

def loadVerifiedData(request):
    verifiedStores_list = Stores.objects.filter(is_verified=1)
    jsonVerifiedData = []
    for store in verifiedStores_list:
        storeDict = {'id': store.id, 'name': store.name, 'latitude': store.latitude,
        'longitude': store.longitude, 'address': store.address, 'created_at': store.created_at,
        'updated_at': store.updated_at, 'is_verified': store.is_verified,
        'metadata': store.metadata, 'source': store.source}
        jsonVerifiedData.append(storeDict)
    return JsonResponse({'verified_data': jsonVerifiedData})

def loadUnverifiedData(request):
    unverifiedStores_list = Stores.objects.filter(is_verified=0)
    jsonUnverifiedData = []
    for store in unverifiedStores_list:
        storeDict = {'id': store.id, 'name': store.name, 'latitude': store.latitude,
        'longitude': store.longitude, 'address': store.address, 'created_at': store.created_at,
        'updated_at': store.updated_at, 'is_verified': store.is_verified,
        'metadata': store.metadata, 'source': store.source}
        jsonUnverifiedData.append(storeDict)
    return JsonResponse({'unverified_data': jsonUnverifiedData})

# def loadResetData(request, id):
#     resetData = Stores.objects.get(pk=id)
#     jsonResetData = {'id': resetData.id, 'name': resetData.name, 'latitude': resetData.latitude,
#     'longitude': resetData.longitude, 'address': resetData.address, 'created_at': resetData.created_at,
#     'updated_at': resetData.updated_at, 'is_verified': resetData.is_verified, 'metadata': resetData.metadata,
#     'source': resetData.source}
#     return JsonResponse(jsonResetData) 

  
class StoresDetailView(generic.DetailView):
    model = Stores
    template_name = 'StoreTinder/detail.html'
    context_object_name = 'store'

class EditStoreView(generic.UpdateView):
    model = Stores
    fields = ['name', 'latitude', 'longitude', 'address', 'source', 'metadata', 'created_at', 'updated_at', 'is_verified']
    template_name = 'StoreTinder/update.html'
    context_object_name = 'store'