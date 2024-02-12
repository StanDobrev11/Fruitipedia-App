from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from fruitipediaapp.fruits.forms import CreateFruitForm


# Create your views here.
def create_fruit(request):
    create_fruit_form = CreateFruitForm(request.POST or None, user=request.user)

    if request.method == 'POST':
        if create_fruit_form.is_valid():
            create_fruit_form.save()
            return redirect('dashboard')

    context = {
        'create_fruit_form': create_fruit_form,
    }
    return render(request, 'fruits/create-fruit.html', context)


def details_fruit(request, fruit_id):
    context = {}
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_id):
    context = {}
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    context = {}
    return render(request, 'fruits/delete-fruit.html', context)
