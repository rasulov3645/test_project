from django.shortcuts import render

# Create your views here.


def landing(request):
    name = "Gamzat"
    corrent_day = "03.01.2017"
    return render(request, 'landing/landing.html', locals())


