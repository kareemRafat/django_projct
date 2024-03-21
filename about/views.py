from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.db.models import Q


# Create your views here.
def index(request) :
    return render(request , 'about/index.html' , {
        'users' : User
                    .objects
                    # .filter(Q(address = 'mansoura') | Q(email = 'kareem@gmail.com'))
                    .filter(username__contains = 'a')
                    .filter(tall__range = (10,35))
                    .order_by('username') , 
        'email' : User.objects.count() ,
        'test' : '<p>kareeeeeem</p>'
    })

def show(request , id):
    return render(request , 'about/show.html' , {
        'user' : User.objects.get(id = id)
    })