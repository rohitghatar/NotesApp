from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests, random
from django.core.mail import send_mail
from NotesApp import settings

status = False

# Create your views here.
def index(request):
    #signup code
    global status
    
    
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            newuser = signupform(request.POST)
            if newuser.is_valid():
                newuser.save()
                print('SignUp Successfully')
                messages.success(request,'Signup Successfully')
                status =True
            else:
                print(newuser.errors)
                messages.success(request,'Error, Some thing went wrong')
                status = False

        elif request.POST.get('signin')=='signin':
            # login code
            unm=request.POST['email']
            pas=request.POST['password']

            #fnm=signup.objects.get(email=unm)
            #print(f"Firstname:{fnm.email}")
            user=signup.objects.filter(email=unm,password=pas)
            # fnm=signup.objects.get('firstname')
            # print(f"Firstname:{fnm}")
            userid=signup.objects.get(email=unm)
            print("UserID:",userid.id)
            if user: #true
                print("Login Successfully!")
                request.session['user']=unm
                request.session['userid']=userid.id
                return redirect('notes')
            else:
                print("Error")
            user=request.session.get('user')
            userid=request.session.get('userid')
            try:
                cuser=signup.objects.get(id=userid)
                return render(request,'index.html',{'status':status,'user':user,'userid':cuser})
            except:
                return render(request,'index.html',{'status':status,'user':user})
    user=request.session.get('user')
    return render(request,'index.html',{'status':status,'user':user})

def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        newnotes=notesForm(request.POST,request.FILES)
        if newnotes.is_valid():
            newnotes.save()
            print("Your notes has been submitted!")
        else:
            print(newnotes.errors)
    
    return render(request,'notes.html',{'user':user})

# userid = None
# user = None

# cuser=signup.objects.get(id=userid)

def profile(request):
    user=request.session.get('user')
    userid=request.session.get('userid')
    try:
        cuser=signup.objects.get(id=userid)
        return render(request,'profile.html',{'user':user,'userid':cuser})
    except:
        return render(request,'profile.html',{'user':user})

def about(request):
    user=request.session.get('user')
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get('user')

    if request.method=='POST':
        newfeedback=feedbackForm(request.POST)
        if newfeedback.is_valid():
            newfeedback.save()
            print("Your FEEDBACK has been submitted!")

            #Email Send
            send_mail(subject="Thank you!",message=f"Dear User\n\nThanks for connecting with us!\nIf you have any queries regarding service, Please contact on\n\n+919624144412 | rohitghatar@gmail.com | www.tops-int.com",from_email=settings.EMAIL_HOST_USER,recipient_list=[request.POST['email']])

            #SMS Send
            otp=random.randint(1111,9999)
            # url = "https://www.fast2sms.com/dev/voice"
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"jy1lum4IfY6henACTQa3wBZROiXtkDLocVU57GdrKM0HbSsxpv7Hp0ZtaeNj23drDVfoPu1KGQgsMB64","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['phone']}"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
        else:
            print(newfeedback.errors)

    return render(request,'contact.html',{'user':user})


def userlogout(request):
    logout(request)
    return redirect('/')