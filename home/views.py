from django.shortcuts import redirect, render

from lottery.models import Category, Lottery
from order.models import Winner


def home(request):

    lottary_data = {
        "lottary_img": "https://cdn.pristinecompetitions.co.uk/wp-content/uploads/2024/05/WebImage_BlackChaser-768x768.jpg",
        "draw_date":"DRAW Jan 12",
        "lottary_name" : "Lottary Name",
        "lottary_cash" : 20000,
        "per_entry" : 20,
        "sold" : 75,
    }
    catagories = Category.objects.all()
    
    return render(request, 'index.html', context={'catagories':catagories})
    



def winners_view(request):

    winners = Winner.objects.all().order_by('-id')
    return render(request, 'winners.html', context={'winners':winners})



def recent_tickets(request):

    return render(request, 'components/recent-tickets.html')

