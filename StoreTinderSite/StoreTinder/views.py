from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from .models import Stores
from django.core.paginator import Paginator
from django.utils import timezone
import json
import os.path

# Create your views here.
def index(request):
    return render(request, 'StoreTinder/home.html')

def loadAllStoresData(request):
    verifiedStores_list = Stores.objects.filter().order_by("-id")
    storeFeatures = []
    path = "/static/StoreTinder/images"
    imagePath = ""
    for store in verifiedStores_list:
        imagePath = os.path.join(path, store.source + ".png")
        storeDict = {
                        "type": "Feature",
                        "properties": {
                            "id": store.id,
                            "title": store.name,
                            "address": store.address,
                            "source": store.source,
                            "is_verified": store.is_verified,
                            "iconImage": imagePath,
                            "iconSize": [40,40]
                        },
                        "geometry": {
                            "coordinates": [
                                store.longitude,
                                store.latitude
                            ],
                            "type": "Point"
                        }
                    }
        storeFeatures.append(storeDict)
    return JsonResponse({"type": "FeatureCollection", "features": storeFeatures})

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

