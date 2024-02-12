from django.shortcuts import render


# Create your views here.
def create_profile(request):
    context = {}
    return render(request, 'profiles/create-profile.html', context)


def edit_profile(request):
    context = {}
    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    context = {}
    return render(request, 'profiles/delete-profile.html', context)


def details_profile(request):
    context = {}
    return render(request, 'profiles/details-profile.html', context)
