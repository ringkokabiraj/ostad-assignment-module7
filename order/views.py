import json

from django.shortcuts import redirect, render

from .models import *


def checkout_view(request):

    if request.method=="GET":
        return render(request,'checkout.html')
    if request.method=="POST":
        data = request.POST
        cart_data = request.COOKIES.get('cart')
        json_data = json.loads(cart_data)
        print(json_data)
        if json_data:
            pass
        else:
            return redirect('/cart/')
        order = Order.objects.create(date_of_birth = data['dob'],first_name = data['firstName'],last_name = data['lastName'],
                                     country = data['country'],street_address=data['address1'],address_line2=data['address2'],
                                     town = data['city'],postcode = data['postcode'], phone=data['phone'],
                                     email=data['email'])
        
        if request.user.is_authenticated:
            order.user = request.user
        for i in json_data:
            try:
                product = Lottery.objects.get(id = i['id'])
            except:
                continue
            OrderItem.objects.create(order = order, product=product, quantity = i['quantity'])
        if 'emailUpdates' in data:
            if data['emailUpdates'] == 'on':
                order.sign_me_up = True
    return render(request, 'payment.html')

    
