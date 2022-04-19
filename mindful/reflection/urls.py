from django.urls import path, include
from .views import FormReflectionView, DashboardView, ReflectionEntryViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'entries', ReflectionEntryViewSet, basename='entry')

urlpatterns = [
    path('', FormReflectionView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('api/', include(router.urls)),
]