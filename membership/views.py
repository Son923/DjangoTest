from django.shortcuts import render
from django.http import HttpResponse
from account.models import User

def index(request):
    user = User.objects.get(email="nson@gmail.com")
    print(user.badges_earned)
    return HttpResponse(user.__dict__)
