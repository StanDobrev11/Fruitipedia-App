from django.shortcuts import render


# Create your views here.
def create_fruit(request):
    context = {}
    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request):
    context = {}
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request):
    context = {}
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request):
    context = {}
    return render(request, 'fruits/delete-fruit.html', context)
