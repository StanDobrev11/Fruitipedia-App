from django.shortcuts import render

from fruitipediaapp.fruits.models import Fruit


# Create your views here.
def index(request):
    context = {}
    return render(request, 'common/index.html', context)


def dashboard(request):
    user_fruits = Fruit.objects.all()

    context = {
        'user_fruits': user_fruits
    }
    return render(request, 'common/dashboard.html', context)
