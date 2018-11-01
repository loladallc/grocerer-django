# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
# Create your views here.
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

def index(request):
    return HttpResponse("This is the owner page")


@csrf_exempt
@require_http_methods(["POST"])
def register_store(request):
    if request.method == "POST":
        if request.content_type == "application/x-www-form-urlencoded":
            params = request.POST
            print(params)
            print(params.get("username"))
        else:
            params = request.body
            print(json.loads(params)["username"])
        return HttpResponse(params)
