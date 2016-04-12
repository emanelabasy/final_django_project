from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .forms import ArticleForm
from .forms import UserForm2


#to use Date.....
# from datetime import date,timedelta

#to use filtering.........
# from django.utils.translation import ugettext_lazy as _

# start_date = date.today()
# end_date = (start_date+timedelta(days=6))
# old_date = date(2016,1,1)


#-------------------Change Activation---------------------------
def change_active(ModelAdmin,request,queryset):
	queryset.update(is_active = 1)
	change_active.short_description = "Change to active"	
	
def change_deactive(ModelAdmin,request,queryset):
	queryset.update(is_active = 0)
	change_deactive.short_description = "Change to deactive"	



# --------Define an inline admin descriptor for UserProfile model----------

class User_profileInline(admin.StackedInline):
    model = User_profile
    can_delete = False
    verbose_name_plural = 'user_profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (User_profileInline, )
    list_display =["username","first_name","last_name","email","is_active"]
    actions = [change_active,change_deactive]
    form = UserForm2

#---------Publish Action--------
def make_published(ModelAdmin, request, queryset):
	queryset.update(art_status='p')
	make_published.short_description = "Mark selected articles as published"

#---------Approve Action-----------
def make_approved(ModelAdmin, request, queryset):
	queryset.update(art_status='a')
	make_approved.short_description = "Mark selected articles as approved"

		
# #--------Filtering By Date--------------
# class PublishDateFilter(admin.SimpleListFilter):

#     title = _('Publish Date')
#     parameter_name = 'publish_date'

#     def lookups(self, request, model_admin):

#         return (
#             ('this_week', _('This Week')),
#             ('oldest', _('Oldest')),
#         )

#     def queryset(self, request, queryset):

#         if self.value() == 'this_week':
#             return queryset.filter(art_publish_date__range=[start_date, end_date])

#         if self.value() == 'oldest':
#             return queryset.filter(art_publish_date__range=[end_date, old_date])



#--------Filtering By Status--------------
# class PublishStatusFilter(admin.SimpleListFilter):

#     title = _('Publish Status')
#     parameter_name = 'publish_state'

#     def lookups(self, request, model_admin):

#         return (
#             ('drafts', _('Drafts')),
#             ('publish', _('Published')),
#         )

#     def queryset(self, request, queryset):

#         if self.value() == 'drafts':
#             return queryset.filter(art_status__exact='d')

#         if self.value() == 'publish':
#             return queryset.filter(art_status__exact='p')



#-----------to edit article form ---------
class ArticleAdmin(admin.ModelAdmin):
	list_display = ["art_title","art_publish_date","art_status",
					"art_number_views","comments_count"]
	form = ArticleForm
	### actions:
	actions = [make_published,make_approved]

	##filters:
	list_filter = ('art_status','art_publish_date')


admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Banwords)
admin.site.unregister(User)
admin.site.register(lockSystem)
admin.site.register(User, UserAdmin)
