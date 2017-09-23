from rest_framework import routers
from django.conf.urls import url
from person.views import PersonViewSet

router = routers.SimpleRouter()
router.register(r'persons', PersonViewSet)
urlpatterns = router.urls
