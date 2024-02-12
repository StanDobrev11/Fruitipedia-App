from django import forms

from fruitipediaapp.profiles.models import Profile


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class CreateProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'email',
            'password']

        labels = {
            'first_name': False,
            'last_name': False,
            'email': False,
            'password': False
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class EditProfileForm(BaseProfileForm):
    class Meta(BaseProfileForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'image_url',
            'age'
        ]

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
            'age': 'Age',
        }
