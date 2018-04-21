from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile, Address, CreditCard
from localflavor.us.forms import USStateSelect, USZipCodeField
from django.forms import inlineformset_factory

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)

    def save(self, commit=True):
        user = super(SignUpUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class SignUpProfileForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    phone = forms.CharField(max_length=16)

    class Meta:
        model = Profile
        fields = ('birth_date', 'phone',)
        exclude = ('user',)

    def save(self, commit=True):
        profile = super(SignUpProfileForm, self).save(commit=False)
        profile.birth_date = self.cleaned_data['birth_date']
        profile.phone = self.cleaned_data['phone']

        if commit:
            profile.save()

        return profile


class AddressForm(forms.ModelForm):
    address = forms.CharField(max_length=20, required=True)
    state = USStateSelect()
    city = forms.CharField(max_length=20)
    zipcode = USZipCodeField()

    class Meta:
        model = Address
        fields = ('address', 'state', 'city', 'zipcode')
        exclude = ('user',)

    def save(self, commit=True):
        address = super().save(commit=False)
        address.address = self.cleaned_data.get('address')
        address.state = self.cleaned_data.get('state')
        address.city = self.cleaned_data.get('city')
        address.zipcode = self.cleaned_data.get('zipcode')

        if commit:
            address.save()

        return address

class CreditCardForm(forms.ModelForm):
    card_name = forms.CharField(max_length=36)
    card_number = forms.CharField(max_length=26)
    card_expirydate = forms.DateField()
    card_ccv = forms.CharField(max_length=3)

    class Meta:
        model = CreditCard
        fields = ('card_name', 'card_number', 'card_expirydate', 'card_ccv')
        exclude = ('user',)

    def save(self, commit=True):
        creditcard = super().save(commit=False)
        creditcard.card_name = self.cleaned_data.get('card_name')
        creditcard.card_number = self.cleaned_data.get('card_number')
        creditcard.card_expirydate = self.cleaned_data.get('card_expirydate')
        creditcard.card_ccv = self.cleaned_data.get('card_ccv')

        if commit:
            creditcard.save()

        return creditcard


class UserViewForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'birth_date',
            'phone'
        )

class AddressViewForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address', 'state', 'city', 'zipcode')
        exclude = ('user',)

class CreditCardViewForm(forms.ModelForm):
    class Meta:
        model = CreditCard
        fields = ('card_name', 'card_number', 'card_expirydate', 'card_ccv')
        exclude = ('user',)

class EditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )
        exclude = ('password',)

        def clean_password(self):
            return ""

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'birth_date',
            'phone',
        )
        exclude = ('password',)


class EditAddressForm(UserChangeForm):
    class Meta:
        model = Address
        fields = ('address', 'state', 'city', 'zipcode')
        exclude = ('user',)

class EditCreditCardForm(UserChangeForm):
    class Meta:
        model = CreditCard
        fields = ('card_name', 'card_number', 'card_expirydate', 'card_ccv')
        exclude = ('user',)