from django import forms
from .models import Team
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Your password must contain at least 8 characters."
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Enter the same password as before, for verification."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = [
            'member1',
            'member2',
            'member3',
            'member4',
            'member5',
            'member6',
            'subject1',
            'subject2',
            'subject3',
        ]

    def clean(self):
        cleaned_data = super().clean()
        subjects = set([cleaned_data.get('subject1'), cleaned_data.get('subject2'), cleaned_data.get('subject3')])

        if len(subjects) < 3:
            raise forms.ValidationError('At least three different subjects must be selected.')

        return cleaned_data
