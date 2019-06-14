from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome! Please select the language you would like to translate")

def landing(request):
	context = {
	}
	return render(request, 'landing/index.html', context)