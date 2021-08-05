from django.http import HttpResponse 
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import LocationForm

def locationView(request):
    if request.method == 'GET':
        form = LocationForm()
    else:
        form = LocationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            number = form.cleaned_data['number']
            about = form.cleaned_data['about']
            try:
                send_mail(name, email, about, ['cassandratalbot@yahoo.co.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('rating.html/')
    return render(request, "location.html", {'form': form})

def ratingView(request, *args, **kwargs):
    return render(request, "rating.html/",)
