from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from fruitipediaapp.profiles.forms import CreateProfileForm, EditProfileForm
from fruitipediaapp.profiles.models import Profile


# Create your views here.
def create_profile(request):
    create_profile_form = CreateProfileForm(request.POST or None)

    if request.method == 'POST':
        if create_profile_form.is_valid():
            user = User.objects.create_user(
                username=request.POST['first_name'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
            profile = create_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # auto login upon signup
            login(request, user)

            return redirect('dashboard')

    context = {
        'create_profile_form': create_profile_form
    }
    return render(request, 'profiles/create-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.get(email=request.user.email)
    edit_profile_form = EditProfileForm(request.POST or None, instance=profile)

    if request.method == 'POST':
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return redirect('dashboard')

    context = {
        'edit_profile_form': edit_profile_form
    }
    return render(request, 'profiles/edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.get(email=request.user.email)

    if request.method == 'POST':
        request.user.delete()
        profile.delete()
        logout(request)
        return redirect('index')

    context = {}
    return render(request, 'profiles/delete-profile.html', context)


def details_profile(request):
    profile = Profile.objects.get(email=request.user.email)

    context = {
        'profile': profile
    }
    return render(request, 'profiles/details-profile.html', context)
