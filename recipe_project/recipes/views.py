from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.

def recipes_detail(request):
    if request.method =="POST":

        data = request.POST
        title = data.get('title')
        description = data.get('description')
        ingredients = data.get('ingredients')
        image = request.FILES.get('image')

        Recipe.objects.create(
            title = title,
            description = description,
            ingredients = ingredients,
            image = image,
        )
        return redirect('/recipes_detail/')
    queryset = Recipe.objects.all()
    context = {'recipes_detail':queryset}
    return render(request,'recipes_detail.html',context)

def display_recipe(request):
    QLRO=Recipe.objects.all()
    d={'QLRO':QLRO}
    
    return render(request, 'display_recipe.html',d)