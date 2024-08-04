from django.shortcuts import render,redirect
from .forms import Sign_Up_Form , profile_form, user_form
from django.contrib.auth import aauthenticate, login
from .models import Profile

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = Sign_Up_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = aauthenticate(username=username, password=password)
            login(request, user)
            return redirect('/accounts')
    else:
        form = Sign_Up_Form()
    return render(request, 'registration/signup.html', {'form': form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userForm = user_form(request.POST , instance=request.user)
        profileForm = profile_form(request.POST , instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myform = profileForm.save(commit=False)
            myform.user = request.user
            myform.save()
            return redirect('/accounts/profile')
    else:
        userForm = user_form(instance=request.user)
        profileForm = profile_form(instance=profile)
    return render(request, 'profile/profile_edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})