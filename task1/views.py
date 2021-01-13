from django.shortcuts import render
from .models import Service
# Create your views here.


def index(request):

    boxed = Service.objects.all()

    return render(request, "index.html", {'boxed': boxed})