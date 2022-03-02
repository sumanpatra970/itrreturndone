from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from .form import account_creation_form
from .form import login_form,password_form,user_change_form
# Create your views here.
def home(request):
    if request.method=='POST':
        user_fm=login_form(data=request.POST)
        if user_fm.is_valid():
            uname=user_fm.cleaned_data['username']
            upass=user_fm.cleaned_data['password']
            user=auth.forms.authenticate(username=uname,password=upass)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('account')
            else:
                user_fm=login_form()
                return HttpResponse("something went wrong")
        else:
                user_fm=login_form()
                return HttpResponse("something went")
    else:
        user_fm=login_form()
        return render(request,'home.html',{'fm':user_fm})
    
def signup(request):
    if request.method=="POST":
        fm=account_creation_form(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'account.html')
        else:
            fm=account_creation_form()
            return render(request,'ok.html',{'fm':fm})
    else:
        fm=account_creation_form()
        return render(request,'signup.html',{'fm':fm})

def account(request):
    if request.user.is_authenticated:
        user_acc=user_change_form(instance=request.user)
        return render(request,'account_detail.html',{'data':user_acc})
    else:
        return HttpResponseRedirect('login')
