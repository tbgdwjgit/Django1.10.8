from django.conf.urls import url
from webdev.views import first_page

urlpatterns = [
    url(r'^$',first_page),
]
