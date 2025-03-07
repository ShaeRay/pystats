from django.urls import path, include
from rest_framework import routers
from .views import UploadedFileViewSet,StatsView,TTestView, AnovaView,CorrelationView

router = routers.DefaultRouter()
router.register('upload', UploadedFileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', StatsView.as_view(), name='stats'),
    path('corr/', CorrelationView.as_view(), name='correlation'),
    path('ttest/', TTestView.as_view(), name='ttest'),
    path('anova/', AnovaView.as_view(), name='anova'),
]