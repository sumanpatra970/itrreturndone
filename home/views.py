from django.shortcuts import render

from django.contrib import auth

from django.http import HttpResponseRedirect,HttpResponse

from home.models import itrrequest

from .form import loginform, signupform

from .form import user_change_form,itrform,itroform

from django.http import FileResponse

from django.contrib import messages

import razorpay

from django.contrib.auth.models import User

from fpdf import FPDF

def home(request):
    context = {}
    form = loginform(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=auth.forms.authenticate(username=uname,password=upass)
            if user is not None:
                auth.login(request,user)
                messages.success(request,'Your login is successful')
                return HttpResponseRedirect('home')
            else:
                messages.success(request,'username or password is invalid')
                return render(request, "home.html", context)
    return render(request, "home.html", context)

def signup(request):
    context = {}
    form = signupform(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email=  form.cleaned_data.get("email")
            password= form.cleaned_data.get("password")
            print(username,password,email)
            try:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'Your account is successfully created')
                return render(request,'account.html')
            except:
                messages.success(request,'username is not unique')
                return render(request, "signup.html", context)
        else:
            return render(request, "signup.html", context)
    return render(request, "signup.html", context)

def account(request):
    if request.user.is_authenticated:
        user_acc=user_change_form(instance=request.user)
        return render(request,'account_detail.html',{'data':user_acc})
    else:
        return HttpResponseRedirect('login')

def itrhome(request):
    return render(request,'itrhome.html')

def itrdetails(request):
    if request.method=="POST":
        fm=itroform(request.POST or None, request.FILES or None)
        if fm.is_valid():
            fm.save()
            print("good")
            return HttpResponseRedirect('paymentstart')
        else:
           return HttpResponse("something went") 
    else:
        user_fm=itrform()
        return render(request,'itrform.html',{'fm':user_fm})

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

def testing(request):
    return render(request,'index.html')

def formtesting(request):
    context = {}
    form = signupform(request.POST or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email=  form.cleaned_data.get("email")
            password= form.cleaned_data.get("password")
            print(username,password,email)
            user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
            user.save()
    return render(request, "formtest.html", context)

def formtesting2(request):
    context = {}
    form = itroform(request.POST or None,request.FILES or None)
    context['form'] = form
    if request.POST:
        if form.is_valid():
            fathername = form.cleaned_data.get("fathername")
            dob= form.cleaned_data.get("dob")
            state = form.cleaned_data.get("state")
            city = form.cleaned_data.get("city")
            bank = form.cleaned_data.get("bankname")
            ifsc = form.cleaned_data.get("ifsc")
            pan = form.cleaned_data.get("pan")
            account = form.cleaned_data.get("account")
            aadhar = form.cleaned_data.get("aadhar")
            user=itrrequest.objects.create(FatherName=fathername,DateOfBirth=dob,
            state=state,city=city,pan=pan,aadhar=aadhar,bankname=bank,
            bankaccount=account,ifsccode=ifsc,form16=request.FILES['form16'])
            user.save()
            return HttpResponseRedirect("paymentstart")
    return render(request, "formtest2.html", context)

