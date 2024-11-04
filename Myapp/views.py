from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import auth
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.template.loader import render_to_string
from django.core.mail import send_mail, BadHeaderError
from verify_email.email_handler import send_verification_email
from django.core.mail import EmailMessage, get_connection
# Create your models here.
def register(request):
 
    if request.user.is_authenticated:
        return redirect("/login/")
     
    if request.method == 'POST':
        form = RegForm(request.POST)
 
        if form.is_valid():
            
          
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email already taken ')
                return redirect('register')
           
        
            
            else:
                form.save()
                user = authenticate(email=email,password = password)
                auth.login(request, user)
                # user = User.objects.create(username=username, email=email, password=password)
                
                inactive_user = send_verification_email(request, form)

                messages.success(request, "Vendor Profile and wallet created successfully ")
                messages.info(request, "Please check your email for account activation ")
                return redirect('/login/')
            
         
        else:
            return render(request,'registration.html',{'form':form})
     
    else:
        form = RegForm()
        return render(request,'registration.html',{'form':form})
    


def login(request):

    # if request.user.is_authenticated:
    #     return redirect('/login/')
     
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)
 
        if user is not None:
            auth.login(request,user)
            return redirect('/login/')
        else:
            messages.error(request, 'invalid login details')
            form = AuthenticationForm()
            return render(request,'login.html',{'form':form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})
    
    
 
def logout(request):
    request.session.clear()
    return redirect('login')