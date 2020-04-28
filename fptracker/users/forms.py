from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from users.models import Profile

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
        )

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'history_text',
            'favorite_text',
        )
        labels = {
            'history_text':'How long have you been using fountain pens?',
            'favorite_text':'What is your favorite pen?'
        }