from django.urls import path

from .views import home, pullrequests

urlpatterns=[
    path('',home,name='home'),
    path('pullrequests/',pullrequests,name="pullrequests")
]