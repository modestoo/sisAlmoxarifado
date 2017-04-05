from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^material/novo/$', views.novo_material, name='novo_material')
]