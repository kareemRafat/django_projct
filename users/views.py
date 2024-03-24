from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login , logout
# Create your views here.

# register
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

# login
def login_views(request):
    if request.method == "POST" : 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #! login() from django.contrib.auth
            login(request , form.get_user()) 
            return redirectToNext(request) # my function
    else :
        form = AuthenticationForm()

    return render(request , 'login.html', {
        'form' : form
    })

# logout
def logout_views(request):
    if request.method == "POST":
        logout(request)
        return redirect('users:login')
    else :
        return redirect('about:index')
    
# redirect when login to the next page
def redirectToNext(request):
    if 'next' in request.POST :
        return redirect(to = request.POST.get('next'))
    else :
        return redirect(to = 'about:index')
