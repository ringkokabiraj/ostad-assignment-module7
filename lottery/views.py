from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Category, Lottery


def view_lottery(request,pk):

    try:
        lottery = Lottery.objects.get(id=pk)
    except(ObjectDoesNotExist):
        return redirect('/')
    
    return render(request,'single_product.html', context={'lottery':lottery})
