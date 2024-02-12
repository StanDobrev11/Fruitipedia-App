from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from fruitipediaapp.fruits.forms import CreateFruitForm, EditFruitForm, DeleteFruitForm
from fruitipediaapp.fruits.models import Fruit


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
    fruit = get_object_or_404(Fruit, pk=fruit_id)
    context = {
        'fruit': fruit
    }
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, fruit_id):
    fruit = get_object_or_404(Fruit, pk=fruit_id)

    edit_fruit_form = EditFruitForm(request.POST or None, instance=fruit)
    if request.method == 'POST':
        if edit_fruit_form.is_valid():
            edit_fruit_form.save()
            return redirect('dashboard')

    context = {
        'edit_fruit_form': edit_fruit_form,
        'fruit': fruit
    }
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, fruit_id):
    fruit = get_object_or_404(Fruit, pk=fruit_id)
    delete_fruit_form = DeleteFruitForm(request.POST or None, instance=fruit)

    if request.method == 'POST':
        delete_fruit_form.save()
        return redirect('dashboard')

    context = {
        'delete_fruit_form': delete_fruit_form,
        'fruit': fruit,
    }
    return render(request, 'fruits/delete-fruit.html', context)
