from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
#! login_required decorators like a middleware
@login_required(login_url='users:login')
def index(request) :
    return render(request , 'index.html' , {
        'users' : User
                    .objects
                    # .filter(Q(address = 'mansoura') | Q(email = 'kareem@gmail.com'))
                    .filter(username__contains = 'a')
                    .filter(tall__range = (10,35))
                    .order_by('username') , 
        'email' : User.objects.count() ,
        'test' : '<p>kareeeeeem</p>'
    })

@login_required(login_url='users:login')
def show(request , id):
    return render(request , 'show.html' , {
        'user' : User.objects.get(id = id)
    })