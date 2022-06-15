from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=20, required=True)

def index(request):
    context = {}
    context["name"] = "Crate"
    views_list = ["Django課程","Python課程","C++課程"]
    context["views_list"] = views_list
    views_dic = {"name":"Crate","age":25}
    context["views_dic"] = views_dic
    emptyList = []
    context["emptyList"] = emptyList
    return render(request, "index.html", context)
def test(request):
    context = {}
    context["name"] = "Crate"
    return render(request, "test.html", context)
# Create your views here.
