from django.urls import path
from django.urls import path, include
from mywatchlist.views import show_html
from mywatchlist.views import show_xml 
from mywatchlist.views import show_json

app_name = 'mywatchlist'

urlpatterns = [
    path('', include('mywatchlist.urls')),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]