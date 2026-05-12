from django.shortcuts import render

# Create your views here.
from .models import Page

def page_view(request, page_id):
    page=Page.objects.get(id=page_id)
    
    return render(request, 'pages/page.html',{'page':page})

def home_view(request):
    pages= Page.objects.all()
    
    return render(request, 'pages/home.html', {'pages':pages})
