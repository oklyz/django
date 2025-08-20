from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat
from django.views.generic.edit import CreateView , DeleteView, UpdateView
# Create your views here.

class CatCreate(CreateView):
    model = Cat
    # fields = "__all__"
    fields = ["name", "breed", "description", "age", "image"]
    # success_url = "/cats/"

class CatUpdate(UpdateView):
    model = Cat
    fields = ["breed", "description", "age"]

class CatDelete(DeleteView):
    model = Cat
    success_url = "/cats/"

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def cats_index(request):
    # SELECT * FROM "main_app_cat"
    cats = Cat.objects.all() # .find()
    return render(request, "cats/index.html", {"cats": cats})

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, "cats/detail.html", {"cat": cat})
