from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect
from .forms import (
    SignUpUserForm, SignUpProfileForm, UserProfileForm, UserViewForm,
    EditProfileForm, EditForm, AddressForm, CreditCardForm,
    AddressViewForm, CreditCardViewForm)
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse
from .models import Address, CreditCard
from django.forms import modelform_factory


def signup(request):
    if request.method == 'POST':
        user_form = SignUpUserForm(request.POST)
        profile_form = SignUpProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()

            profile = profile_form.save(commit=False)

            #Clean Profile
            user.profile.birth_date = profile_form.cleaned_data.get('birth_date')
            user.profile.phone = profile_form.cleaned_data.get('phone')
            user.profile.save()


            address_form = AddressForm(request.POST)
            if address_form.is_valid():
                address = address_form.save(commit=False)
                address.user = user.profile.user

                #Clean Address
                address.address = address_form.cleaned_data.get('address')
                address.state = address_form.cleaned_data.get('state')
                address.city = address_form.cleaned_data.get('city')
                address.zipcodezipcode = address_form.cleaned_data.get('zipcode')

                address.save()

            creditcard_form = CreditCardForm(request.POST)
            if creditcard_form.is_valid():
                creditcard = creditcard_form.save(commit=False)
                creditcard.user = user.profile.user

                creditcard.card_name = creditcard_form.cleaned_data.get('card_name')
                creditcard.card_number = creditcard_form.cleaned_data.get('card_number')
                creditcard.card_expirydate = creditcard_form.cleaned_data.get('card_expirydate')
                creditcard.card_ccv = creditcard_form.cleaned_data.get('card_ccv')

                creditcard.save()

            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        user_form = SignUpUserForm()
        profile_form = SignUpProfileForm()
        address_form = AddressForm()
        creditcard_form = CreditCardForm()

    return render(request, 'registration/signup.html',
              {'user': user_form, 'profile': profile_form,
               'address': address_form, 'creditcard': creditcard_form})


@login_required
def profile(request):
    user_form = UserViewForm(instance= request.user)
    profile_form = UserProfileForm(instance= request.user.profile)

    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = Address(user=request.user)
    address_form = AddressViewForm(instance=address)

    try:
        creditcard = CreditCard.objects.get(user=request.user)
    except CreditCard.DoesNotExist:
        creditcard = CreditCard(user=request.user)
    creditcard_form = CreditCardViewForm(instance=creditcard)

    args = {'user': user_form, 'profile': profile_form,
            'address': address_form, 'creditcard': creditcard_form}
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

