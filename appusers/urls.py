from django.conf.urls import url
from appusers.views import registro_view

urlpatterns = [
    url(r'^registrar/$', registro_view,name="registro"),
]
