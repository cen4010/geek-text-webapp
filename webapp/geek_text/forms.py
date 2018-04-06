from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    phone = forms.IntegerField()
    city = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birth_date', 'city', 'phone')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date' , 'phone' , 'city')


class EditUserForm(UserChangeForm):
    template_name='/something/else'

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Profile
        fields = (
            'birth_date',
            'city',
            'phone'
        )
