# from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *

def show_about_us(request):
    print("about page request")
    name = "Learn with Krishn"
    link = 'https://www.UniverseKnowledge.com/KrishnaGyan'
     
    data = { 
        'name': name,
        'link': link
    }
    
    return render(request, "about.html", data)


def show_home_page(request):
    cats = Category.objects.all()
    images =Image.objects.all()
    data = {
        'images': images,
        'cats': cats
    }

    return render(request, 'home.html', data)

def show_category_page(request, cid):
    cats = Category.objects.all()
    
    category = Category.objects.get(pk=cid)
    
    images =Image.objects.filter(cat=category)  
    data = {
        'images': images,
        'cats': cats
    }

    return render(request, 'home.html', data)

def search_images(request):
    query = request.GET.get('q')  # Get the search term from the request
    cats = Category.objects.all()
    
    if query:
        images = Image.objects.filter(title__icontains=query)  # Search by title
    else:
        images = Image.objects.all()
    
    data = {
        'images': images,
        'cats': cats,
        'query': query
    }
    
    return render(request, 'home.html', data)


def home(request):
    return redirect('/home')
    