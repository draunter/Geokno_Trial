from django.conf.urls import url
from . import views

app_name = 'Input'

urlpatterns = [

    url(r'^$',views.func,name = "homepage"),
    url(r'^search/',views.search, name="search"),
    url(r'^tst/$',views.map, name="map"),
    url(r'^query/$',views.query,name="query")

]


