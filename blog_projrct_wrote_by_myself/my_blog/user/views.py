import json
from random import random

from django.shortcuts import render

# Create your views here.
from django.views import View


class UserView(View):
    pass


def sms_view(request):
    json_str = request.body
    json_obj = json.loads(json_str)
    phone = json_obj['phone']
    code = random.randint(100000, 999999)
