from django.conf.urls import url
from . import views   #relatively import from views

urlpatterns =[
url(r'^$',views.index,name="index")]  #views in file and . index is function in it