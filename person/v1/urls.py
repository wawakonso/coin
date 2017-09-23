from django.conf.urls import url

urlpatterns = [
    url(r'^v1', include('person.v1.persons.urls')),    
]
