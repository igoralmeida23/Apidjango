from django.conf.urls import url
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^getpessoas/$', views.GetPessoas.as_view(), name='getpessoas'),
    url(r'^cadastro/$', views.Cadastro.as_view(), name='cadastro'),
]