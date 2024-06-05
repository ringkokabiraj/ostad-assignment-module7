from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from authentication.models import User

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="GET":
        return render(request,'login.html')
    else:
        email = request.POST['email']
        password = request.POST['password']

        user = user = authenticate(email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,'User Not Found .')
        return redirect('/auth/login')
    

def register_view(request):
    if request.method == "GET":
        return render(request, 'register.html')
    
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email = email)
        if user.exists():
            messages.error(request,'Email Already Exists.')
            return redirect('/auth/register')
        
        user = User.objects.create(email=email)
        user.set_password(password)
        user.save()
        # except:
        #     messages.error(request, 'Something Went Wrong!')
        #     return redirect('/auth/register')
        
        return redirect('/auth/login')


    

def logout_view(request):

    logout(request)
    return redirect('/')