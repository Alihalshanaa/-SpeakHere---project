from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def handlelogin (request):
    if request.method=="POST":

        username=request.POST['username']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('post-list')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/handlelogin')

    
    return render(request,'auth/handlelogin.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
      
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'auth/signup.html')
            
            
        try:
            if User.objects.get(username=username):


                messages.warning(request,"UserName is Taken")
                return render(request,'auth/signup.html')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return render(request,'auth/signup.html')

        except Exception as identifier:
            pass
        
        myuser = User.objects.create_user(username,email,password)
        
        myuser.save()
        messages.info(request,"Signup SuccessFull! Please Login ")
        return redirect('/auth/handlelogin/')

    return render(request,'auth/signup.html')

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('/auth/handlelogin')