from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddUser, LogUser
from .models import User, Item, Category
from django.shortcuts import get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core import serializers
import re


def index(request):
    return render(request, "cash_register/index.html")
    
@login_required
def home(request):
    page_title = "Cash Register"
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, "cash_register/home.html", {"items": items,
                                                "categories": categories,
                                                "page_title": page_title,},)
@login_required
def inventory(request):
    page_title = "Inventory"
    json_serializer = serializers.get_serializer("json")()
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    selected = Item.objects.filter(is_sold=False)[0]
    return render(request, "cash_register/inventory.html", {"page_title": page_title,
                                                     "items": items,
                                                     "selected": selected,
                                                     "categories": categories},)
    
@login_required
def statistics(request):
    page_title = "Statistics"
    return render(request, "cash_register/statistics.html", {"page_title": page_title,},)

@login_required
def suppliers(request):
    page_title = "Suppliers"
    return render(request, "cash_register/suppliers.html", {"page_title": page_title,},)
    
@login_required
def customers(request):
    page_title = "Customers"
    return render(request, "cash_register/customers.html", {"page_title": page_title,},)

@login_required
def settings(request):
    page_title = "Settings"
    return render(request, "cash_register/settings.html", {"page_title": page_title,},)


def login(request):
    if request.method == "POST":
        form = LogUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Authentication
            try:
                user = User.objects.get(username=username)
                if user.password != password:
                    messages.error(request,'Invalid password')
                    return redirect("/login")
            except User.DoesNotExist:
                user = None
            # If authentication is successful Login
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"{username} Logged In Successfully!")
                return redirect("home")
            else:
                messages.error(request, "Cannot Log In!")
                return redirect("/login")
    else:
        form = LogUser()
    return render(request, 'cash_register/login.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = AddUser(request.POST)
        if form.is_valid():
            # Get user data from the form
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm']
            # Check if email is valid
            email_pattern = re.compile(r'[a-z0-9_./]+@{1}[a-z0-9#]+.[a-z0-9]{2,5}')
            if re.fullmatch(email_pattern, email):
                # Check whether the password is valid
                password_pattern = re.compile(r'[A-Za-z0-9~`!@#$%^&*()_+={[}]|\:;"\'<,>.?/]+')
                if password_pattern.search(password) and len(password) >= 8:
                    # Check if the password is equal to the confirm  password
                    if password == confirm:
                        new = User(username=username, email=email, password=password)
                        new.save()
                        messages.success(request, "Account Created Successfully!")
                    else:
                        messages.error(request, "Passwords Don't match!")
                else:
                    messages.error(request, "Invalid password!")
                    messages.info(request, "Passwords should contain any of the four character types:   uppercase letters: (A-Z), lowercase letters: (a-z), numbers (0-9), and symbols (~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/)")
            else:
                messages.error(request, "Invalid Email!")
                messages.info(request,"Acceptable email prefix formats: Allowed characters: letters (a-z), numbers, underscores, periods, and dashes. Acceptable email domain formats Allowed characters: letters, numbers, dashes. The last portion of the domain must be at least two characters, for example: .com, .org, .cc")
        return redirect("/signup")
    else:
        form = AddUser()
    return render(request, 'cash_register/signup.html', {'form':form})


def logout(request):
    auth_logout(request)
    return redirect("/")