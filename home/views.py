from django.shortcuts import render,redirect



def home(request):

    lottary_data = {
        "lottary_img": "https://cdn.pristinecompetitions.co.uk/wp-content/uploads/2024/05/WebImage_BlackChaser-768x768.jpg",
        "draw_date":"DRAW Jan 12",
        "lottary_name" : "Lottary Name",
        "lottary_cash" : 20000,
        "per_entry" : 20,
        "sold" : 75,
    }

    return render(request, 'index.html', context=lottary_data)
    

def competitions(request):

    return render(request, 'competitions.html')

def winners(request):

    return render(request, 'winners.html')

def cart(request):

    return render(request, 'cart.html')

def single_product(request):

    return render(request, 'single_product.html')