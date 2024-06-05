from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


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
    

def logout_view(request):

    logout(request)
    return redirect('/')