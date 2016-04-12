from django import forms
from .models import *

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    image = forms.ImageField()

class CommentForm(forms.Form):
    comment = forms.CharField()
    
class ReplyForm(forms.Form):
    parentcomment = forms.IntegerField()
    reply = forms.CharField()
 