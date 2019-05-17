from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator
from django.utils import timezone
import json
# Create your views here.

def index(request):
    return render(request, "reacts/index.html")