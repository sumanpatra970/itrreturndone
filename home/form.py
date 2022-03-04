from django import forms

from django.contrib.auth.models import User

from django.core.validators import MaxLengthValidator

from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm

from .models import itrrequest

from datetime import date

from django.core.validators import FileExtensionValidator

class account_creation_form(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=None
    class Meta:
        model = User
        fields =['username','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'})}
        def __init__(self, *args, **kwargs):
            super(UserCreationForm, self).__init__(*args, **kwargs)
            self.fields['email'].required = True

class loginform(forms.Form):
    username=forms.CharField(required=True,error_messages = {'required':"Please enter  username"}, 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':" username"}))
    password=forms.CharField(error_messages = {'required':"Please enter password"}, 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"password"}))

class signupform(forms.Form):
    username=forms.CharField(required=True,error_messages = {'required':"Please enter  username"}, 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':" username"}))
    password=forms.CharField(error_messages = {'required':"Please enter password"}, 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Password"}))
    email=forms.CharField(required=True,error_messages = {'required':"Please enter email"}, 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"email"}))

class password_form(PasswordChangeForm):
    old_password=None
    new_password1=forms.CharField(label="Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="Confirm Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User

class user_change_form(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email','first_name','last_name',]
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                }

class itrform(forms.ModelForm):
    class Meta:
        model=itrrequest
        fields=['FatherName','DateOfBirth','state','city','pan','aadhar','bankname','bankaccount','ifsccode','form16']
        widgets={'FatherName':forms.TextInput(attrs={'class':'form-control op','placeholder':"Father's name"}),
                'DateOfBirth':forms.DateInput(attrs={'class':'form-control op','placeholder':"Date Of Birth",'type':'date'}),
                'state':forms.TextInput(attrs={'class':'form-control op','placeholder':"Enter state"}),
                'city':forms.TextInput(attrs={'class':'form-control op','placeholder':"Enter City"}),
                'pan':forms.TextInput(attrs={'class':'form-control op','placeholder':"PAN"}),
                'aadhar':forms.TextInput(attrs={'class':'form-control op','placeholder':"Aadhar no"}),
                'bankname':forms.TextInput(attrs={'class':'form-control op','placeholder':"Bank Name"}),
                'bankaccount':forms.TextInput(attrs={'class':'form-control op','placeholder':"Bank Account no"}),
                'ifsccode':forms.TextInput(attrs={'class':'form-control op','placeholder':"IFSC"}),
                'form16':forms.FileInput(attrs={'class':'form-control op','placeholder':"form 16"}),
                }
        def __init__(self, *args, **kwargs):
                super(itrform, self).__init__(*args, **kwargs)
                self.fields['FatherName'].label = ""
                self.fields['DateOfBirth'].label = ""
                self.fields['state'].label = ""
                self.fields['city'].label = ""
                self.fields['pan'].label = ""
                self.fields['aadhar'].label = ""
                self.fields['bankname'].label = ""
                self.fields['bankaccount'].label = ""
                self.fields['ifsccode'].label = ""
                self.fields['form16'].label = "upload form-16"

def checkaadhar(value):
    if len(value)!=12:
        raise forms.ValidationError("enter correct aadhar no")

def checkdob(value):
    today = date.today()
    print("Today's date:", today,value)
    if value>today:
        raise forms.ValidationError("you can not enter future date")

class itroform(forms.Form):
    fathername=forms.CharField(error_messages = {'required':"Please enter father name"},validators=[MaxLengthValidator(50)], 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Father's Name"}))
    dob=forms.DateField(error_messages = {'required':"Please enter dob"},validators=[checkdob], 
    widget=forms.DateTimeInput(attrs={'class':'form-control','placeholder':"Date Of Birth",'type':'date'}))
    state=forms.CharField(error_messages = {'required':"Please enter state"},validators=[MaxLengthValidator(50)], 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"State name"}))
    city=forms.CharField(error_messages = {'required':"Please enter city"},validators=[MaxLengthValidator(50)], 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"City name"}))
    pan=forms.CharField(error_messages = {'required':"Please enter pan no"},validators=[MaxLengthValidator(50)], 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"PAN no"}))
    bankname=forms.CharField(error_messages = {'required':"Please enter bank name"},validators=[MaxLengthValidator(50)], 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Bank name"}))
    ifsc=forms.CharField(error_messages = {'required':"Please enter bankIFSC code"},validators=[MaxLengthValidator(50)], 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Bank IFSC code"}))
    account=forms.CharField(error_messages = {'required':"Please enter account no"},validators=[MaxLengthValidator(50)], 
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Bank Account No"}))
    aadhar=forms.CharField(error_messages = {'required':"Please enter aadhar no"},validators=[checkaadhar] ,
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Aadhar no"}))
    form16=forms.FileField(label='Upload form-16',validators=[FileExtensionValidator(allowed_extensions=['pdf'])],error_messages = {'required':"Please upload form16"},widget=forms.FileInput(attrs={'class':'form-control pcd','placeholder':"upload Form16"}))
    def __init__(self, *args, **kwargs):
        super(itroform, self).__init__(*args, **kwargs)
        self.fields['fathername'].label = ""
        self.fields['dob'].label = ""
        self.fields['state'].label = ""
        self.fields['city'].label = ""
        self.fields['pan'].label = ""
        self.fields['aadhar'].label = ""
        self.fields['bankname'].label = ""
        self.fields['account'].label = ""
        self.fields['ifsc'].label = ""