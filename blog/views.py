from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Notice
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')
    # messages.success(request, 'This is a test messsage')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('user_name', '')
        email = request.POST.get('user_email', '')
        phone = request.POST.get('user_phone', '')
        message = request.POST.get('user_message', '')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, 'Your form has been submitted successfully!')
    return render(request, 'blog/contact.html')

def notice(request):
    col_notice = Notice.objects.all()
    print(col_notice)
    return render(request, 'blog/notice.html', {'col_notice':col_notice})


def handleReg(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        faculty = request.POST.get('faculty_option')


        if len(username) > 8:
            messages.info(request,"Your username should only be 8 character long")
            return redirect('/')

        if not username.isalnum():
            messages.info(request,"Try entering alphanumeric entities")
            return redirect('/')
        
        if pass1!=pass2:
            messages.info(request,"Password fields must be same")
            return redirect('/')
        
        ouruser = User.objects.create_user(username, email, pass1)
        ouruser.first_name = fname
        ouruser.last_name = lname
        ouruser.c_faculty = faculty
        ouruser.save()



        messages.success(request,"You have been successfully registered as a student")
        return redirect('/')
    
    else:
        return HttpResponse("404 not found! Unable to connect to the server")
        


def handleLogin(request):
    if request.method == 'POST':
        login_username = request.POST['login_username']
        login_password = request.POST['login_password']

        user = authenticate(username=login_username, password=login_password)
        if user is not None:
            login(request,user)
            messages.success(request,f"Successfully logged in")
            return redirect('/')
        
        else:
            messages.info(request, "Invalid credentials!")
            return redirect("/")

def handlelogout(request):
    logout(request)
    messages.info(request,"Successfully logged out!")
    return redirect('/')
    
def user_profile(request):
    return render(request,"blog/user_profile.html")


    
 



