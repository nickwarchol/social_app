from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    welcome = 'Welcome to pEarth'

    context = {
        'welcome': welcome,
        'user' : user,
    }
    return render(request, 'main/home.html', context)