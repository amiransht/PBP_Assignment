from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers


# TODO: Create your views here.
def show_html(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'list_film': data_watchlist,
        'nama': 'Amira Nisrina',
        'id': '2106703815'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
