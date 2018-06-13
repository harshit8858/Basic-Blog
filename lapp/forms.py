from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='must be unique', required=True, widget=forms.EmailInput(attrs={'placeholder':'E-Mail', 'class':'form-control', 'style':'width:200px'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class': 'form-control', 'style':'width:200px'}), label="Password", required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','class': 'form-control', 'style':'width:200px'}), label="Confirm Password", required=True)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username','class': 'form-control', 'style':'width:200px'}), label="Username", required=True)
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control', 'style':'width:200px'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control', 'style':'width:200px'}))

    def clean_email(self):
        mail = self.cleaned_data['email']
        try:
            match = User.objects.get(email__iexact=mail)
        except:
            return mail
        raise forms.ValidationError("Email already exists.")

    class Meta:
        model = User
        fields = (
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',
                  )


class Boxform(forms.ModelForm):
    # s_no = forms.IntegerField(required=True, max_value=999999, widget=forms.NumberInput(attrs={'placeholder':'Pincode', 'class':'form-control', 'style':'width:200px'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'URL','class':'form-control','style':'width:400px;'}))
    image = forms.FileField(required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Description', 'style':'resize:none;width:400px;height:200px','class':'form-control'}))
    title = forms.CharField(max_length=400,widget=forms.TextInput(attrs={'placeholder': 'Title','class':'form-control','style':'width:400px;'}))
    # likes =
    # dislikes =
    # created_at =

    class Meta:
        model = Box
        fields = ['title',
                  'content',
                  'url',
                  'image',
                 ]


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Old password",
        required=True)

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New password",
        required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm new password",
        required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_password']

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile_pic
        fields = ['p_pic']