from django.urls import path

from .views import index, pullrequests, calculate

urlpatterns=[
    path('',index,name='index'),
    path('pullrequests/',pullrequests,name="pullrequests"),
    path('calculate',calculate,name="calculate")
]