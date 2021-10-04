from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .forms import RegistrationFrom,AccountLoginForm,AccountUpdate


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationFrom(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=  email , password = raw_password)
            login(request,account)#, backend='django.contrib.auth.backends.ModelBackend'
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationFrom()
        context['registration_form'] = form
    return render(request,'accounts/register.html',context)

def logout_view(request):
    logout(request)
    return redirect('home')
    

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user =authenticate(email= email , password = password)
            if user:
                login(request,user)
                return redirect('home')
    else:
        form = AccountLoginForm()
    context['login_form'] = form
    return render(request,"accounts/login.html",context)

def account_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {}
    if request.POST:
        form = AccountUpdate(request.POST,instance = request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdate(
            initial = {
                'email':request.user.email,
                'username':request.user.username,
            }
        )
    context['account_form'] = form
    return render(request,"accounts/account.html",context)
