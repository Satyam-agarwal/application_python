from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns =[
url(r'^$',ListView.as_view(queryset=Post.objects.all(),template_name="blog/blog.html")),

url(r'^(?P<pk>\d+)$',DetailView.as_view(model= Post,template_name="blog/post.html"))

]# ?P named groups regular expressions
  #pk = primary key that is 1  ; \d+ = one or more digits