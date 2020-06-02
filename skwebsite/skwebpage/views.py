from django.shortcuts import render

# Create your views here.
def index(request): 
    return render(request,'index.html')

def aboutus(request):   
    return render(request, 'aboutus.html')

def academy(request):   
    return render(request, 'academy.html')

def auditing(request):   
    return render(request, 'auditing.html')

def solutions(request):   
    return render(request, 'solutions.html')

def syservices(request):   
    return render(request, 'syservices.html')

def blog(request):   
    return render(request, 'blog.html')

def gallery(request):   
    return render(request, 'gallery.html')

def contact(request):   
    return render(request, 'contact.html')