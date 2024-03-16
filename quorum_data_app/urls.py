from django.urls import path
from .api import viewset

urlpatterns = [
    path('legislator_info/', viewset.legislator_info, name='legislator_info_api'),
    path('bill_info/', viewset.bill_info, name='bill_info_api'),
]
