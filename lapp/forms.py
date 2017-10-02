from django import forms
from django.contrib.auth.models import User
from .models import *


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True,max_length=30)))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True,max_lentgth=30)))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=30,render_value=False)))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=30,render_value=False)))

    def clean_username(self):
        n = self.cleaned_data['username']

        try:
            match = User.objects.get(username__iexact=n)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("username already exist!")


    def clean_email(self):
        mail = self.cleaned_data['email']

        try:
            match = User.objects.get(username__iexact=mail)
        except:
            return self.cleaned_data['email']
        raise forms.ValidationError("email already exist!")

    def clean(self):
        if 'password1' in  self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError('didnt matched..try again!')
            return self.cleaned_data

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Boxform(forms.ModelForm):
    # title=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'title', 'placeholder': 'Title','class':'form-control','style':'width:300px;'}))
    # content=forms.CharField(widget=forms.Textarea(attrs={'id':'content','placeholder':'Whats on your Mind!','rows': 4, 'cols': 50, 'style':'resize:none;width:300px;','class':'form-control'}))
    # pic = forms.FileField(required=False)

    class Meta:
        model = Box
        fields = ['title','content','pic']


class Profileform(forms.ModelForm):
    job = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'job'}))
    address = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'address'}))
    profile_pic = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'profile_pic'}))
    number = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'id':'number'}))
    class Meta:
        model = Profile
        exclude = ['user','password']
        #fields = ['job','address','profile_pic','number']

'''
class Loginform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(render_value=False)) #####

    class Meta:
        model = User
        #widget = { 'password': forms.PasswordInput(),}
        fields = '__all__'
'''


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

class ChangeForm(forms.ModelForm):
    class Meta:
        model = like
        fields = '__all__'
