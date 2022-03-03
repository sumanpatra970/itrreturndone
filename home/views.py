from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from .form import account_creation_form
from .form import login_form,password_form,user_change_form,itrform
from django.http import FileResponse
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
                return HttpResponseRedirect('home')
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

def itrhome(request):
    return render(request,'itrhome.html')

def itrdetails(request):
    if request.method=='POST':
        fm=itrform(request.POST or None, request.FILES or None)
        if fm.is_valid():
            fm.save()
            print("good")
            return HttpResponseRedirect('paymentstart')
        else:
           return HttpResponse("something went") 
    else:
        user_fm=itrform()
        return render(request,'itrform.html',{'fm':user_fm})

import razorpay
from django.contrib.auth.models import User
def itrsubmit(request):
     return HttpResponseRedirect('paymentstart')

def payment(request):
    context={}
    notes = {'Shipping address': 'Bommanahalli, Bangalore'}
    client = razorpay.Client(auth=("rzp_test_mEqDIf8ehJFOX5", "0EL1uE9m44CYcSQJEwUvmEfA"))
    response = client.order.create(dict(amount=100, currency='INR', receipt='order_rcptid_11', notes=notes, payment_capture='0'))
    order_id = response['id']
    order_status = response['status']
    if order_status=='created':
        context['product_id'] = "product"
        context['price'] = 100
        context['name'] = request.user
        context['email'] = User.objects.get(username=request.user).email
        context['order_id'] = order_id
        return render(request, 'confirm_order.html', context)
    return HttpResponse('<h1>Error in  create order function</h1>')

def payment_status(request):
    response = request.POST
    client = razorpay.Client(auth=("rzp_test_mEqDIf8ehJFOX5", "0EL1uE9m44CYcSQJEwUvmEfA"))
    params_dict = {
        'razorpay_payment_id' : response['razorpay_payment_id'],
        'razorpay_order_id' : response['razorpay_order_id'],
        'razorpay_signature' : response['razorpay_signature']
    }
    x=response['razorpay_payment_id']
    y=response['razorpay_order_id']
    try:
        status = client.utility.verify_payment_signature(params_dict)
        return render(request, 'order_summary.html', {'status': 'Payment Successful','x':x,'y':y})
    except:
        return render(request, 'order_summary.html', {'status': 'Payment Faliure!!!'})

from fpdf import FPDF
def invoice(request):
    pdf = FPDF()   
    pdf.add_page()
    pdf.set_font("Arial", size = 15)

    f = open("bill.txt", "r")
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
    
    pdf.output("billing.pdf")   
    try:
        return FileResponse(open('ca.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        return HttpResponse('file not found')
