# from __future__ import unicode_literals
# from django.db import models
# from django.contrib.auth.models import User
# # from captcha.fields import CaptchaField
# # from . import AnyOtherField
# from django import forms
# # Create your models here.

# class User_profile (models.Model):
# 	user_img=models.ImageField(blank=True)
# 	user=models.OneToOneField(User)

# 	# def __str__(self):
# 	# 	return user.username
# #-------------------------------------------------------------------
# class Article(models.Model):
# 	art_title=models.CharField(max_length=255)
# 	art_content=models.TextField()
# 	art_img=models.ImageField(upload_to='static/img/')
# 	art_status=models.CharField(max_length=50)
# 	art_publish_date=models.DateTimeField(auto_now_add=True)
# 	art_number_views=models.IntegerField(default=0)
# 	art_user_id=models.ForeignKey(User_profile,on_delete=models.CASCADE)
# 	def __str__(self):
# 		 return self.art_title
# #-------------------------------------------------------------
# class Mark(models.Model):
#     user_id = models.IntegerField()
#     article_id = models.IntegerField()
# #-------------------------------------------------------------------

# class Keywords(models.Model):
# 	keyword_name=models.CharField(max_length=255)
# 	keyword_art_id=models.ManyToManyField(Article)
# 	def __str__(self):
# 		 return self.keyword_name
# #-------------------------------------------------------------------		 

# class Comment(models.Model):
# 	Comment_content=models.TextField()
# 	Comment_status=models.BooleanField(default=1)
# 	Comment_parent_id=models.IntegerField()
# 	Comment_user_like=models.ManyToManyField(User_profile)
# 	Comment_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
# 	def __str__(self):
# 		 return self.Comment_content
# #-------------------------------------------------------------------		 

# class  Banwords(models.Model):
# 	banword_name=models.CharField(max_length=255)
# 	def __str__(self):
# 		 return self.banword_name

# #-------------------------------------------------------------------

# class Emotions(models.Model):
# 	emotion_letter=models.CharField(max_length=255)
# 	emotion_img=models.CharField(max_length=255)
# 	def __str__(self):
# 		 return self.emotion_letter
# #-------------------------------------------------------------------
# # class CaptchaTestForm(forms.Form):
# #     myfield = AnyOtherField()
# #     captcha =CaptchaField()

# #-------------------------------------------------------------------

# # class Employee(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     department = models.CharField(max_length=100)

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

#to use signals.....
from django.db.models import signals
from articles.signals import count_changes

STATUS_CHOICES = (
    ('d', 'Drafts'),
    ('p', 'Published'),
    ('a', 'Approved'),
)

class User_profile (models.Model):
	user_img=models.ImageField(blank=True)
	user=models.OneToOneField(User)
		

class Article(models.Model):
	art_title=models.CharField('title',max_length=255)
	tag_name = models.CharField(max_length=30,default=" ")
	art_content=models.TextField()
	art_img=models.ImageField(upload_to='static/img/')
	art_status=models.CharField('publish status',max_length=1,choices=STATUS_CHOICES,default='d')
	art_publish_date=models.DateTimeField('publish date',auto_now_add=True)
	art_number_views=models.IntegerField('view count',default=0)
	art_user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	#---------counter------------------------------
	comments_count = models.IntegerField(default=0, editable=False)

  	def count_changes(self):
	    count = self.comment_set.filter(Comment_status=True).count()
	    self.comments_count = count
	    self.save()
	def __str__(self):
		 return self.art_title

# class Article(models.Model):
# 	art_title=models.CharField(max_length=255)
# 	art_content=models.TextField()
# 	art_img=models.ImageField(upload_to='static/img/')
# 	art_status=models.CharField(max_length=50)
# 	art_publish_date=models.DateTimeField(auto_now_add=True)
# 	art_number_views=models.IntegerField(default=0)
# 	art_user_id=models.ForeignKey(User_profile,on_delete=models.CASCADE)***
# 	def __str__(self):
# 		 return self.art_title
#-----------------------------------------------------

class Mark(models.Model):
    user_id = models.IntegerField()
    article_id = models.IntegerField()
		 

class keywords(models.Model):
	keyword_name=models.CharField(max_length=255)
	# keyword_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
	keyword_art_id=models.ManyToManyField(Article)

	def __str__(self):
		 return self.keyword_name


class Comment(models.Model):
	Comment_content=models.TextField()
	Comment_status=models.BooleanField('Is Approved',default=1)
	Comment_parent_id=models.IntegerField(default=-1)
	user_comment_like=models.ManyToManyField(User)
	Comment_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
	def __str__(self):
		 return self.Comment_content


# class Comment(models.Model):
# 	Comment_content=models.TextField()
# 	Comment_status=models.BooleanField(default=1)
# 	Comment_parent_id=models.IntegerField('self',on_delete=models.CASCADE,default= -1)
# 	Comment_user_like=models.ManyToManyField(User_profile)*****
# 	Comment_art_id=models.ForeignKey(Article,on_delete=models.CASCADE)
# 	def __str__(self):
# 		 return self.Comment_content


signals.post_save.connect(count_changes, sender=Comment)
signals.post_delete.connect(count_changes, sender=Comment)


class  Banwords(models.Model):
	banword_name=models.CharField('BanWord',max_length=255)
	def __str__(self):
		 return self.banword_name


# class  Banwords(models.Model):
# 	banword_name=models.CharField(max_length=255)
# 	def __str__(self):
# 		 return self.banword_name

class Emotions(models.Model):
	emotion_letter=models.CharField(max_length=255)
	emotion_img=models.CharField(max_length=255)
	def __str__(self):
		 return self.emotion_letter

# class Emotions(models.Model):
# 	emotion_letter=models.CharField(max_length=255)
# 	emotion_img=models.CharField(max_length=255)
# 	def __str__(self):
# 		 return self.emotion_letter

class lockSystem(models.Model):
	is_locked = models.BooleanField(default= False)




