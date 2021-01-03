from django.shortcuts import render,HttpResponse
from django.http import request

# Create your views here.
def inicio(request):
	return HttpResponse('Hasta aca todo bien')
	