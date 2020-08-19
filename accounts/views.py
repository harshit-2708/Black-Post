from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_view(request, *args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        account = form.get_user()
        login(request, account)
        return redirect('/')
    context = {
        "form" : form,
        "btn_label":"Login",
        "title":"Login",
    }
    return render(request, "accounts/auth.html", context)

def register_view(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        # send a confirmation email to verify their account
        login(request, user)
        return redirect("/")
    context = {
        "form": form,
        "btn_label": "Register",
        "title": "Register"
    }
    return render(request, "accounts/auth.html", context)

def logout_view(request, *args, **kwargs):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    context = {
        "form": None,
        "description": "are you sure to logout",
        "btn_label":"click to confirm",
        "title":"Logout",
    }
    return render(request, "accounts/auth.html", context)
