from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import SignUpForm, EditProfileForm, EditUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from .forms import UserForm, ProfileForm

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

    return render(request, 'accounts/profile.html',
                  {'user': user_form , 'profile': profile_form } )

@login_required
def edit_profile(request):
    print("FIX ME!!")
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instace=request.user)
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() or profile_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect(reverse('settings:profile'))
    else:
        user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

        args = { 'user': user_form, 'profile': profile_form}
        return render(request, 'accounts/edit_profile.html', args)



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('settings:profile'))
        else:
            return redirect(reverse('settings:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)