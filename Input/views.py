from django.shortcuts import render
from django.http.response import HttpResponse
from .models import AirborneLidar, DEM
from django.views import generic
import os
import pandas as pd
from bokeh.io import show, output_file
from bokeh.models import ( GMapPlot, GMapOptions, ColumnDataSource, Range1d,DataRange1d, Circle, PanTool, WheelZoomTool, PolySelectTool, BoxSelectTool, Square )
import googlemaps
import urllib.request, json


latitude=0
longitude=0
# Create your views here.
def func(request):
    return render(request,'Input/Homepage.html')

def search(request):
    location = request.POST['search']
    api_key = 'AIzaSyB4WAP0dZG2f6avZ6EYiMBolrtVrxgqtlU'
    gm = googlemaps.Client(key = api_key)
    address = location
    lat = gm.geocode(address)[0]['geometry']['location']['lat']
    lng = gm.geocode(address)[0]['geometry']['location']['lng']


    map_options = GMapOptions(lat=lat,lng=lng, map_type = 'roadmap' , zoom=8)

    plot = GMapPlot(x_range = Range1d(),
                    y_range = Range1d(),
                    map_options = map_options,
                    api_key = api_key)

    plot.add_tools(PanTool(),WheelZoomTool(), BoxSelectTool(), PolySelectTool() )
    scale = 2.5
    source = ColumnDataSource(data = dict(lat = [lat],
                                          lon= [lng],
                                          rad = [2],
                                          size = [100]
                                          ))

    circle = Circle(x=lng,
                    y=lat,
                    size = "rad",
                    fill_color='red',
                    fill_alpha=0.5)
    global latitude, longitude
    latitude = lat
    longitude = lng
    square=Square(x=lng,y=lat, size = "size",fill_color="red", fill_alpha=0.5)

    plot.add_glyph(source, square)
    output_file('C:/Users/Mudit/PycharmProjects/Geokno_trial/Input/templates/Input/plot.html')
    return render(request,'Input/Query.html')


def map(request):
    return render(request,'Input/plot.html')



def query(request):
    return render (request,'Input/Query.html')
