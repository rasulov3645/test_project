from django.shortcuts import render

from .forms import SubcriberForm

# Create your views here.


def landing(request):
    name = "Gamzat"
    corrent_day = "03.01.2017"
    form = SubcriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form)
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])

        new_form = form.save()


    return render(request, 'landing/landing.html', locals())


