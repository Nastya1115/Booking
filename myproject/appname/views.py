from django.shortcuts import render
from django.http import HttpResponse
from appname.models import *

# Create your views here.


def main_page(request):
    context = {

    }
    return render(
        request,
        template_name="basic.html",
        context=context
    )