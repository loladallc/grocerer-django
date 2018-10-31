# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# Create your views here.
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("This is the owner page")


@csrf_exempt
def register_store(request):
    if request.method == "POST":
        params = request.POST
        pprint(params)
        return HttpResponse(params)
