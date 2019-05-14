
# from django.conf.urls import url
from django.urls import path,include

from django.contrib import admin
from ns1 import views as comm
urlpatterns = [
    path('home/',comm.home),
    path('ns1/',comm.ns1),
    path('ns1_3d/',comm.ns1_3d),
    path('germ/',comm.germ),
    path('fungus/',comm.fungus),
    path('plasmid/',comm.plasmid),
    path('cell/',comm.cell),
    path('germ/detail/<str:pre_no>',comm.germ_detail),
    path('plasmid/detail/<str:pre_no>',comm.plasmid_detail),
    path('cell/detail/<str:pre_no>',comm.cell_detail),
    path('ns1_3d/detail/<str:PDB_ID>',comm.ns1_3d_detail),
    path('ns1/list',comm.ns1_list),
    path('ns1/<str:Subtype>',comm.ns1),
    path('ns1/detail/<str:Accession_id>',comm.ns1_detail),
    path('16srna/',comm.r16srna),
    # path('regist',comm.regist),
    # url(r'^', comm.login),
]

