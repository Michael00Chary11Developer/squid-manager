from django.urls import path
from .views import BlockSiteForUser, UserAccessDetail

urlpatterns = [
    path('user/<uuid:user_id>/block_sites/', BlockSiteForUser.as_view(), name='block-sites-for-user'),
    path('user/<uuid:user_id>/access/', UserAccessDetail.as_view(), name='user-access-detail'),
]
