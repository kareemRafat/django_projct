from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login
# Create your views here.

def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid() : 
            user = form.save() # to save to database
            login(request , user) # login after register
            return redirect(to = 'about:index')
    else :
        form = UserCreationForm()  
    return render(request , 'register.html', {
        'form' : form
    })


def login_views(request):
    if request.method == "POST" : 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #! login() from django.contrib.auth
            login(request , form.get_user()) 
            return redirect(to = 'about:index')
    else :
        form = AuthenticationForm()

    return render(request , 'login.html', {
        'form' : form
    })