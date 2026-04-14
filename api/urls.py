from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import LocationViewSet, SafetyReportViewSet, get_safety_score

from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'reports', SafetyReportViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('score/<int:location_id>/', get_safety_score),
]
urlpatterns += [
    
]
urlpatterns+=[
    path('api-token-auth/',obtain_auth_token)
]