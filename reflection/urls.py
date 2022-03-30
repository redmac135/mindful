from django.urls import path, include
from .views import FormReflectionView, DashboardView, ReflectionEntryViewSet
from .router import CustomReflectionEntryRouter

router = CustomReflectionEntryRouter()
router.register(r'entries', ReflectionEntryViewSet, basename='entries')

urlpatterns = [
    path('', FormReflectionView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('api/', include(router.urls)),
]