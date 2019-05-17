from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
import time


# Create your views here.
def index(request):
    data = {'pagename': 'tutorial'}
    return render(request, 'index.html', {'data': json.dumps(data)})


def hello(request):
    person = request.GET.get('name', 'Dzul')
    # return HttpResponse('Hello, {}'.format(person))
    return render(request, 'greeting.html', {"name": person})


def calc(request):
    # body = json.loads(request.body)
    # print(body)
    a = int(request.POST.get('a', 0))
    b = int(request.POST.get('b', 0))
    result = {'result': a + b}
    time.sleep(2)

    return JsonResponse(result)
