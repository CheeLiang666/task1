from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from .models import Stores
from django.core.paginator import Paginator
from django.utils import timezone
import json

# Create your views here.
def index(request):
    return render(request, 'StoreTinder/index.html')

def loadVerifiedData(request):
    verifiedStores_list = Stores.objects.filter(is_verified=1).order_by("-id")
    jsonVerifiedData = []
    for store in verifiedStores_list:
        storeDict = {'id': store.id, 'name': store.name, 'latitude': store.latitude,
        'longitude': store.longitude, 'address': store.address, 'created_at': store.created_at,
        'updated_at': store.updated_at, 'is_verified': store.is_verified,
        'metadata': store.metadata, 'source': store.source}
        jsonVerifiedData.append(storeDict)
    return JsonResponse({'verified_data': jsonVerifiedData})

def loadUnverifiedData(request):
    unverifiedStores_list = Stores.objects.filter(is_verified=0).order_by("-id")
    jsonUnverifiedData = []
    for store in unverifiedStores_list:
        storeDict = {'id': store.id, 'name': store.name, 'latitude': store.latitude,
        'longitude': store.longitude, 'address': store.address, 'created_at': store.created_at,
        'updated_at': store.updated_at, 'is_verified': store.is_verified,
        'metadata': store.metadata, 'source': store.source}
        jsonUnverifiedData.append(storeDict)
    return JsonResponse({'unverified_data': jsonUnverifiedData})

def loadAllStoresData(request):
    stores_list = Stores.objects.filter().order_by("-id")
    jsonStoresData = []
    for store in stores_list:
        storeDict = {'id': store.id, 'name': store.name, 'latitude': store.latitude,
        'longitude': store.longitude, 'address': store.address, 'created_at': store.created_at,
        'updated_at': store.updated_at, 'is_verified': store.is_verified,
        'metadata': store.metadata, 'source': store.source}
        jsonStoresData.append(storeDict)
    return JsonResponse({'data': jsonStoresData})

# def loadResetData(request, id):
#     resetData = Stores.objects.get(pk=id)
#     jsonResetData = {'id': resetData.id, 'name': resetData.name, 'latitude': resetData.latitude,
#     'longitude': resetData.longitude, 'address': resetData.address, 'created_at': resetData.created_at,
#     'updated_at': resetData.updated_at, 'is_verified': resetData.is_verified, 'metadata': resetData.metadata,
#     'source': resetData.source}
#     return JsonResponse(jsonResetData) 

def convertTimeTo12Hours(time):
    timeToken = time.split(":")
    timePreffix = timeToken[0]
    timeIn12Hours = ""
    if len(timePreffix) == 2:
        if timePreffix[0] != "0":
            # for 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
            preffix = int(timePreffix)
            # for 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
            if preffix > 12:
                timeIn12Hours = str(preffix - 12) + ":" + timeToken[1] + " " + "pm"
            # for 12
            elif preffix == 12:
                timeIn12Hours = str(preffix) + ":" + timeToken[1] + " " + "pm"
            # for 10, 11
            else:
                timeIn12Hours = str(preffix) + ":" + timeToken[1] + " " + "am"
        # for 01, 02, 03, 04, 05, 06, 07, 08, 09
        elif timePreffix[0] == "0" and timePreffix[1] != "0":
            preffix = timePreffix[1:]
            timeIn12Hours = preffix + ":" + timeToken[1] + " " + "am"
        # for 00
        else:
            preffix = int(timePreffix)
            timeIn12Hours = str(preffix + 12) + ":" + timeToken[1] + " " + "am"
    return timeIn12Hours

class StoresDetailView(generic.DetailView):
    model = Stores
    template_name = 'StoreTinder/detail.html'
    context_object_name = 'store'

class EditStoreView(generic.UpdateView):
    model = Stores
    fields = ['name', 'latitude', 'longitude', 'address', 'source', 'metadata', 'is_verified']
    template_name = 'StoreTinder/update.html'
    context_object_name = 'store'

    def get_object(self, queryset=None):
        obj = Stores.objects.get(id=self.kwargs['pk'])
        return obj
    
    def form_invalid(self, form):
        print("This is invalid form")
        import pdb
        pdb.set_trace()
        return super().form_invalid(form)

    def form_valid(self, form):
        print("This is valid form")
        # import pdb
        # pdb.set_trace()
        store = form.save(commit=False)
        store.updated_at = timezone.now()
        verify_status = self.request.POST.get("verified_status")
        if verify_status == "verify":
            store.is_verified = True
        else:
            store.is_verified = False
        phone = self.request.POST.get("phone")
        weekdayopen = convertTimeTo12Hours(self.request.POST.get("weekdayopen"))
        weekdayclose = convertTimeTo12Hours(self.request.POST.get("weekdayclose"))
        weekendopen = convertTimeTo12Hours(self.request.POST.get("weekendopen"))
        weekendclose = convertTimeTo12Hours(self.request.POST.get("weekendclose"))
        metadata = {"phone": phone, "weekdayopen": weekdayopen, "weekdayclose": weekdayclose, 
        "weekendopen": weekendopen, "weekendclose": weekendclose}
        store.metadata = json.dumps(metadata)
        store.save()
        return super().form_valid(form)

class CreateNewStoreView(generic.CreateView):
    model = Stores
    fields = ['name', 'latitude', 'longitude', 'address', 'source', 'is_verified']
    template_name = 'StoreTinder/create_store_form.html'

    def form_invalid(self, form):
        print("This is invalid form")
        import pdb
        pdb.set_trace()
        return super().form_invalid(form)

    def form_valid(self, form):
        print("This is valid form")
        store = form.save(commit=False)
        store.created_at = timezone.now()
        store.updated_at = timezone.now()
        verify_status = self.request.POST.get("verified_status")
        if verify_status == "verify":
            store.is_verified = True
        else:
            store.is_verified = False
        phone = self.request.POST.get("phone")
        weekdayopen = convertTimeTo12Hours(self.request.POST.get("weekdayopen"))
        weekdayclose = convertTimeTo12Hours(self.request.POST.get("weekdayclose"))
        weekendopen = convertTimeTo12Hours(self.request.POST.get("weekendopen"))
        weekendclose = convertTimeTo12Hours(self.request.POST.get("weekendclose"))
        metadata = {"phone": phone, "weekdayopen": weekdayopen, "weekdayclose": weekdayclose, 
        "weekendopen": weekendopen, "weekendclose": weekendclose}
        store.metadata = json.dumps(metadata)
        store.save()
        return super().form_valid(form)

