from django.shortcuts import render
from .models import Service
# Create your views here.


def index(request):

    box1 = Service()
    box1.name = 'Queries '
    # box1.img = 'service-icon-01.png'
    box1.desc = 'You can clear out your doubts here. Click below'
    box1.button = 'Click Here'

    box2 = Service()
    box2.name = 'Discover'
    # box2.img = 'service-icon-02.png'
    box2.desc = 'Search and discover more. Click below to discover.'
    box2.button = 'Click Here'

    box3 = Service()
    box3.name = 'learn More'
    # box3.img = 'service-icon-03.png'
    box3.desc = 'You can learn more about these templates here.'
    box3.button = 'Click Here'

    boxed = [box1, box2, box3]

    return render(request, "index.html", {'boxed': boxed})