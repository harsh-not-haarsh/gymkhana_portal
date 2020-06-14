from django.conf.urls import url, include
from rest_framework import routers

from .views import TeamDisplayViewSet

router = routers.SimpleRouter()
router.register(r'team', TeamDisplayViewSet, basename='Team')

urlpatterns = [
    url(r'^api/', include((router.urls))),
]
