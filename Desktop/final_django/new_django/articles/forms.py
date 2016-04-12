from django.db import models
from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm 
# from .models import Article
# from .models import User_profile
from .models import * 

#class form to forgetPassword Form 
class forgetPassForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True)))

class confirmPassForm(forms.Form):
	code = forms.CharField(max_length=10)
    
class confirmUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=dict(max_length=10,placeholder="Enter User Name Here")))

class resetForm(forms.Form):
    reset = forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=10,placeholder="Enter New Password")))
    resetconfirm=forms.CharField(widget=forms.PasswordInput(attrs=dict(max_length=10,placeholder="Enter Confirm Password")))

#-------------------------------------------------------------------

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # ---------only display this fields
        exclude = ['art_number_views']

        # ---------display these fields
        #fields = ['art_title','art_content','art_img','art_status','art_publish_date','art_user_id']  

class UserForm2(forms.ModelForm):
    class Meta:
        model = User_profile
        # ---------only display this fields
        exclude = ['user_profile_img']

#-------------------------------------------------------------------

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    # user_img = forms.FileField(
    #     label='Select a file',
    # )
    class Meta:
        model = User_profile
        # fields = ('another field', '','')
        fields = ['user_img']

#-------------------------------------------------------------------        
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

# class UpdateUserProfileForm(forms.ModelForm):
#     class Meta:
#         model = User_profile
#         exclude = ['user']
#         # fields = ['user_img']