from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^home$',  views.index),
    url(r'^addtravelplan$',  views.addtravelplan),
    url(r'^addtriplogic$',  views.addtripplan),
    url(r'^plan/(?P<plan_id>\d+)$',  views.plandetails),
    url(r'^join/(?P<plan_id>\d+)$',  views.join),
]
