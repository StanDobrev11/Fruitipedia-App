from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'common/index.html', context)


def dashboard(request):
    context = {}
    return render(request, 'common/dashboard.html', context)
