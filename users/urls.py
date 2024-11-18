from django.urls import path
from .views import BlockedSiteList, UnblockSite

urlpatterns = [
    path('blocked_sites/', BlockedSiteList.as_view(), name='blocked-site-list'),
    path('unblock_site/<int:site_id>/', UnblockSite.as_view(), name='unblock-site'),
]
