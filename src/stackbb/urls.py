from django.conf.urls import url
from django.http import HttpResponse


def healthcheck(request):
    return HttpResponse("OK")


urlpatterns = [
    url(r"^health/$", healthcheck),
]
