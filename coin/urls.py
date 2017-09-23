from django.conf.urls import url, include
from django.contrib import admin
#from person.views import validate_id


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('api/', include('person.urls')),
]
