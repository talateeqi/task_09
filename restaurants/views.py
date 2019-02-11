from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm
from django.contrib.auth import signup, signin, signout

def Signup(request):
    form = signup()
    if request.method == 'POST':
        form = signup(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            signin(request, user)
            return redirect("restaurant_list")

    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def Signin(request):
    form = signin()
    if request.method == 'POST':
        form = signin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['[password']
            user = authenticate(username=username, password=password)

    if user is not None:
         Signin(request, user)
    return render('restaurant-list')
    context = {"form", form}
    return render(request, "sigin.html", context)

def signout(request):
    signout(request)
    return redirect("restaurant-list")


def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form = RestaurantForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def restaurant_update(request, restaurant_id):
    restaurant_obj = Restaurant.objects.get(id=restaurant_id)
    form = RestaurantForm(instance=restaurant_obj)
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant_obj)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    context = {
        "restaurant_obj": restaurant_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def restaurant_delete(request, restaurant_id):
    restaurant_obj = Restaurant.objects.get(id=restaurant_id)
    restaurant_obj.delete()
    return redirect('restaurant-list')
