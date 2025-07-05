from django.shortcuts import render

# Create your views here.

def Homepage(request):
    return render(request, 'home.html')

def Aboutpage(request):
    return render(request, 'about.html')

def Resumepage(request):
    return render(request, 'resume.html')

def Portfoliopage(request):
    return render(request, 'portfolio.html')

def Contactpage(request):
    return render(request, 'contact.html')