from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import SignUpForm, UserForm, ProfileForm


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