from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile, Address
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

class EditForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password'
        )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = (
            'birth_date',
            'phone'
        )