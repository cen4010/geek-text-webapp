from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpUserForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    city = forms.CharField(max_length=100)
    phone = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                  'birth_date', 'city', 'phone')

    def save(self, commit=True):
        user = super(SignUpUserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class UserViewForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'birth_date',
            'city',
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
            'city',
            'phone'
        )