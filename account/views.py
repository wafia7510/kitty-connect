from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def user_account(request):
    return HttpResponse("Hellow world")