from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
'''Home view
    Renders the request to home.html'''
@login_required
def home(request):
    return render(request, 'accounts/home.html')

''' 
Register view
    Takes care of the POST and GET cases, respectively.
    The RegistrationForm is assigned to the form.
    For the POST case:
    If the form is valid then save and redirect the user to home. 
    For the GET case:
    past the context dictionary to the template reg_form.html
'''
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)

'''
Decorator requires the user to be logged in.

'''
@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request , 'accounts/profile.html' , args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = EditProfileForm(data= request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('accounts/change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
