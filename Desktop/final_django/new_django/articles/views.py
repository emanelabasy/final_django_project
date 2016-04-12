from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .models import *
from django.conf import settings
from django.contrib.auth import authenticate , login
from .forms import *
from random import randint
from django.core.mail import send_mail , BadHeaderError
from django.shortcuts import redirect
from django.template import RequestContext
from .forms import UserForm, UserProfileForm
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
# Create your views here.

#*****************************************************************************
def randomConfirm(length=3): 
    return randint(100**(length-1), (100**(length)-1))

# ******************************** register ************************************
def register(request):
    return render(request,'articles/register.html')
def registerform(request):
    return render(request,'articles/registration_form.html')

def email_register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)                 #frist form of user
        profile_form = UserProfileForm(data=request.POST)        #second form of User_profile

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():

             # for send to email
            email = user_form.cleaned_data.get("email")
            subject = " Hi ,Congaturation & Wellcome in EEEOS  ARTICLES . "
            global msg
            msg = str(randomConfirm())
            print msg
            fromEmail = settings.EMAIL_HOST_USER
            toEmail = [email]

            try:
                send_mail(subject,msg,fromEmail,toEmail,fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found ???')
             # end send to email 
                
            # to save data in database
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'user_img' in request.FILES:
                profile.user_img = request.FILES['user_img']
            profile.save()
            registered = True

        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'articles/email_register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def face_register(request):

    return render(request,'articles/face_register.html')

# ******************************** login ************************************        
def signin(request):
    context = RequestContext(request)
    if "user_id" in request.session:
         # return render(request, 'articles/home.html',{'user_id':request.session["user_id"]})
         return redirect('http://127.0.0.1:8000/user_action/')
    else:
    # If the request is a HTTP POST, try to pull out the relevant information.
        if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
            username = request.POST['u_name']
            password = request.POST['pass']

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    request.session["user_id"] = user.id
                    if request.POST.get('remember_me') == "checked":
                        request.session.set_test_cookie()
                        if request.session.test_cookie_worked():
                            request.COOKIES['rememberMe'] = request.POST['remember_me']
                    return redirect('http://127.0.0.1:8000/user_action/')
                    
                else:
                    # An inactive account was used - no logging in!
                    return render(request, 'articles/activeAccount.html')
            else:
                # Bad login details were provided. So we can't log the user in.
                return render(request, 'articles/test.html')
        else:
            return render(request,'articles/email_login.html',  context)

#*************************************************************************************         
def home(request):
    #check if the user logged in redirect to home page
    if "user_id" in request.session :
        return  render(request, 'user_action/index.html')
    else:
        return render(request,'user_action/index.html')
    

#forget password function ...
def forgetPass(request):
   
    form = forgetPassForm(request.POST or None)
    if form.is_valid():

        email = form.cleaned_data.get("email")
        subject = " Hi ,Somebody recently asked to reset your Facebook password. "
        global msg
        msg = str(randomConfirm())
        print msg
        fromEmail = settings.EMAIL_HOST_USER
        toEmail = [email]

        try:
            send_mail(subject,msg,fromEmail,toEmail,fail_silently=False)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/confirm/')

    # context = {
    #     "form" : form,
    # }
    return render(request,'articles/forgetPassword.html',{ "form" : form})

def confirm(request):
    form = confirmPassForm(request.POST or None)
    if form.is_valid():
        code = form.cleaned_data.get("code")
        if code == msg :
            print code
            print msg
            return HttpResponseRedirect('/reset/')

    context = {
        "form" : form,
    }
    return render(request,'articles/confirmMail.html',{"form" : form})

def confirm_User(request):
    form = confirmUserForm(request.POST or None)
    global global_user
    if form.is_valid():
        user_name = form.cleaned_data.get("username")
        users=User.objects.all()
        try:
            for user in users:
                if user.username==user_name:
                    global_user=user
                    
                    return HttpResponseRedirect('/forgetPassword/')
        except:
            return render(request,'articles/confirm_user.html',{"form" : form})

        return render(request,'articles/confirm_user.html',{"form" : form})

    return render(request,'articles/confirm_user.html',{"form" : form})


def reset(request):
    form = resetForm(request.POST or None)
    context = {
        "form" : form,
    }
    if form.is_valid():
        reset = form.cleaned_data.get("reset")
        confirm_reset=form.cleaned_data.get("resetconfirm")
        if reset == confirm_reset :
            u = User.objects.get(username__exact=global_user)
            u.password=reset
            u.save()
            request.session["user_id"]=u.id
            return redirect('http://127.0.0.1:8000/user_action/')
    
    return render(request,'articles/resetpassword.html',{"form" : form})

# ******************************** update user profile ************************************
def profile(request):

    return render(request,'articles/profile.html')

def update_profile(request,user_id):
    title="Welcome %s" %(request.user)
    user=get_object_or_404(User,id=user_id)
    profile=get_object_or_404(User_profile,user_id=user_id)
    form_user=UpdateUserForm(request.POST or None, instance=user)
    form_img=UserProfileForm(request.POST or None, instance=profile)
    registered = False
    if form_user.is_valid() and form_img.is_valid():
        user=form_user.save(commit=True)
        profile=form_img.save(commit=True)
        # to save data in database
        user = form_user.save()
        user.save()
        profile = form_img.save(commit=False)
        profile.user = user
        if 'user_img' in request.FILES:
            profile.user_img = request.FILES['user_img']
        profile.save()
        registered = True
    else:
        print form_user.errors, form_img.errors

    return render(request,"articles/update_profile.html",{'tempelate_title':title ,'user':user,'profile':profile,'form_user':form_user ,'form_img':form_img,'registered':registered })
    

#************************************ links **********************************
def index(request):

    return render(request,'articles/index.html')

def login(request):
    # return HttpResponse("Hello, world. You're at the article index.")
    return render(request,'articles/login.html')

    
def email_login(request):

    return render(request,'articles/email_login.html')


def face_login(request):

    return render(request,'articles/face_login.html')

# ******************************** article ************************************

def view_selected_article(request,art_id):
    article = Article.objects.get(pk=art_id)
    art_tag_text = article.tag_name
    art_tags = art_tag_text.split(" ")
    art_tag = art_tags[0]
    tags = []
    words = article.art_content.split(" ")
    x = 1
    
    #getting the tag keyword
    for word in words: 
        if word == art_tag:
            tags.append(article.art_title)
            # tags.insert(0,word)

    length = len(tags)      
    
    i = 0
    urls = []
    articles = Article.objects.all()
    for art in articles:
        art_words = art.art_title.split(" ")
        for tag in tags:
            if art_tag in art_words:
                urls.append(art.id)

    dictionary ={
        "tags":tags,
        "urls":urls,
        "length":length
    }
    return render(request,"test.html", dictionary)


#--------------------------------------------------------
def is_locked(request):
    lock = lockSystem.objects.get(pk=1)
    if lock.is_locked == True:
        return render(request,"system_locked.html") 
    else:
        return render(request,"test.html")

# ******************************** logout     ************************************        
def logout(request):
    # del request.session["user_id"]
    # return render(request,'articles/login.html')
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session['user_id']
    # else:
        # del request.session['user_id']
    return render(request,'articles/login.html')
# ******************************** END ??? ***********************************        
