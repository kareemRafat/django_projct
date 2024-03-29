from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse
from .models import User
from . import forms
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
#! login_required decorators like a middleware
@login_required(login_url='users:login')
def index(request) :
    return render(request , 'index.html' , {
        'users' : User
                    .objects.all()[0:2], # get from 0 to 2 elements
                    # .filter(Q(address = 'mansoura') | Q(email = 'kareem@gmail.com'))
                    # .filter(username__contains = 'a')
                    # .filter(tall__range = (10,35))
                    # .order_by('username') , 
        'email' : User.objects.count() ,
        'test' : '<p>kareeeeeem</p>'
    })

@login_required(login_url='users:login')
def show(request , id):
    return render(request , 'show.html' , {
        # 'user' : User.objects.get(id = id)
        'user' : get_object_or_404(User, id = id)
    })


@login_required(login_url='users:login')
def new_user(request):
    if request.method == "POST":
        form = forms.NewUser(request.POST , request.FILES)
        if form.is_valid() :
            form.save()
            return redirect(to = 'about:index')
        else:
            return render(request , 'new-user.html' , {'form' : form})
    else :
        form = forms.NewUser()
        return render(request , 'new-user.html' , {'form' : form})