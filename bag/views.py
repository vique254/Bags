# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
 from .models import category,Image
from django.http  import HttpResponse,Http404
# Create your views here.

def home (request):
    return render(request,'home.html')

def search_results(request):
    if  'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories =Image.search_by_name(search_term)
        message = f"{search_term}"
        
        return render (request,'search.html',{"message":message,"category":searched_categories})

    else:
        message = "You haven't searched for any term" 
        return render(request,'search.html',{"message":message})   
    