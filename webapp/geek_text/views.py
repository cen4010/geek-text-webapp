from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserForm, ProfileForm, EditProfileForm, EditUserForm
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
@transaction.atomic
def profile(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    args = {'user_form': user_form, 'profile_form': profile_form }
    return render(request, 'accounts/profile.html', args)


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            request.user.save()
            request.user.profile.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect(reverse('settings:profile'))
        else:
            messages.error(request, ('Please correct the error below.'))

    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def edit_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        #profile_form = EditProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid(): #or profile_form.is_valid():
            user_form.save()
            #profile_form.save()
            return redirect(reverse('settings:profile'))
    else:
        user_form = EditUserForm(instance=request.user)
        #profile_form = EditProfileForm(instance=request.user.profile)
        return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form
    })
