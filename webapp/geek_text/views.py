from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import SignUpUserForm, UserProfileForm, UserViewForm, EditProfileForm, EditForm
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        user_form = SignUpUserForm(request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # load the profile instance created by the signal

            user.profile.birth_date = user_form.cleaned_data.get('birth_date')
            user.profile.city = user_form.cleaned_data.get('city')
            user.profile.phone = user_form.cleaned_data.get('phone')

            user.profile.save()
            user.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        user_form = SignUpUserForm()
    return render(request, 'registration/signup.html', {'user': user_form})

@login_required
def profile(request):
    user_form = UserViewForm(instance= request.user)
    profile_form = UserProfileForm(instance= request.user.profile)
    args = {'user': user_form, 'profile': profile_form}
    return render(request, 'accounts/profile.html', args)


@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = EditForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() or profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect(reverse('view_profile'))
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = EditForm(request.POST, instance=request.user)
        profile_form = EditProfileForm(instance=request.user.profile)

        args = {'user': user_form, 'profile': profile_form }
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

