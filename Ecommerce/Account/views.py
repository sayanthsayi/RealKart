from django.shortcuts import render,redirect
from django.contrib import messages
from . forms import CustomUserForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def Signup(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Signup Successfully! Login to Continue")
            return redirect('login')
    context = {'form':form}
    return render(request,"Signup.html",context)

def Login(request):
    if request.user.is_authenticated:
        messages.warning(request,"you are already logged in")
        return redirect("home")
    else:
        if request.method == 'POST':
            name = request.POST.get('username')
            Password = request.POST.get('password')

            user = authenticate(request,username=name,password=Password)

            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("home")
            
            else:
                messages.error(request,"invalid Username or Password")
                return redirect('login')
    return render(request,"Login.html")

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out in Successfully")
    return redirect('login')
    
