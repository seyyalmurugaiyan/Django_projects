from django.urls import path

from .views import home, pullrequests, calculate

urlpatterns=[
    path('',home,name='home'),
    path('pullrequests/',pullrequests,name="pullrequests"),
    path('calculate',calculate,name="calculate")
]