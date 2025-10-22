from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
# Create your views here.

def recipes_detail(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        ingredients = data.get('ingredients')
        image = request.FILES.get('image')

        Recipe.objects.create(
            title=title,
            description=description,
            ingredients=ingredients,
            image=image,
        )

        messages.success(request, "Recipe added successfully!")
        return redirect('/display_recipe/')
        
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes_detail.html', context)


def display_recipe(request):
    recipes = Recipe.objects.all()

    # Search functionality
    if request.GET.get('search'):
        search_term = request.GET.get('search')
        recipes = recipes.filter(title__icontains=search_term)

    context = {'recipes': recipes}
    return render(request, 'display_recipe.html', context)


def delete_recipe(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    messages.success(request, "Recipe deleted successfully!")
    return redirect('/display_recipe/')


def update_recipe(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        description = data.get('description')
        ingredients = data.get('ingredients')
        image = request.FILES.get('image')

        recipe.title = title
        recipe.description = description
        recipe.ingredients = ingredients

        if image:
            recipe.image = image

        recipe.save()
        messages.success(request, "Recipe updated successfully!") 
        return redirect('/display_recipe/')


    context = {'recipe': recipe}
    return render(request, 'update_recipe.html', context)



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username") 
            return redirect('/login/')
        
        user = authenticate(username = username,password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/') 
        else:
            login(request,user)
            return redirect('/display_recipe/')

    return render(request,'login.html')

def logout_page(request):
    return redirect('/logout/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Username already taken") 
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created successfully!") 
   

    return render(request,'register.html')