import os

from django.conf.urls import url
from django.http import HttpResponse


def healthcheck(request):
    return HttpResponse("OK")


health_path = os.getenv("DJANGO_HEALTH_PATH", "health").strip("/")
health_pattern = r"^{}/$".format(health_path)

urlpatterns = [
    url(health_pattern, healthcheck),
]
