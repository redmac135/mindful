from django.urls import include, path
from rest_framework import routers

from .views import (DashboardView, FormReflectionView,
                    ReflectionEntryListViewSet, ReflectionEntryViewSet)

router = routers.SimpleRouter()
router.register(r'entries', ReflectionEntryViewSet, basename='entry')
router.register(r'all_entries', ReflectionEntryListViewSet, basename='all_entries')

urlpatterns = [
    path('', FormReflectionView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('api/', include(router.urls)),
]
