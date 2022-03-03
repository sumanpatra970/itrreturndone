from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm
from .models import itrrequest

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

class login_form(AuthenticationForm):
    username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))


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
        widgets={'FatherName':forms.TextInput(attrs={'class':'form-control','placeholder':"Father's name"}),
                'DateOfBirth':forms.DateInput(attrs={'class':'form-control','placeholder':"Date Of Birth",'type':'date'}),
                'state':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter state"}),
                'city':forms.TextInput(attrs={'class':'form-control','placeholder':"Enter City"}),
                'pan':forms.TextInput(attrs={'class':'form-control','placeholder':"PAN"}),
                'aadhar':forms.TextInput(attrs={'class':'form-control','placeholder':"Aadhar no"}),
                'bankname':forms.TextInput(attrs={'class':'form-control','placeholder':"Bank Name"}),
                'bankaccount':forms.TextInput(attrs={'class':'form-control','placeholder':"Bank Account no"}),
                'ifsccode':forms.TextInput(attrs={'class':'form-control','placeholder':"IFSC"}),
                'form16':forms.FileInput(attrs={'class':'form-control'}),
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
        self.fields['form16'].label = ""