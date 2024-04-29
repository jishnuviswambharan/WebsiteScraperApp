from django.contrib import messages,auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

#login Page
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        log_user=auth.authenticate(username=username,password=password)

        if log_user is not None:
            auth.login(request,log_user)
            return redirect('/')
        else:
            messages.info(request,"Invalid User Name or Password")
            return redirect('login')
    return render(request,'login.html')

#facebook link
# def facebook(request):
#     return redirect(request,www.facebook.com)

#logout code
def logout(request):
    auth.logout(request)
    return redirect('/')



#Registration Page
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                messages.success(request, "User created successfully")
                print("User created")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
    return render(request, "register.html")