from django.conf.urls import url
from apppublishesandsells.views import index_view,logout_view,login_view

urlpatterns = [
    url(r'^index/$', index_view, name="index"),
    url(r'^logout/$', logout_view, name="logout"),
    url(r'^login/$', login_view, name="login"),
]
