from django.shortcuts import render, HttpResponse

# Create your views here.
def first(request):
    cotexto={'home':'active','about':''}
    return render(request,'home.html',cotexto)
    
def about(request):
    cotexto={'about':'active','home':''}
    return render(request,'about.html',cotexto)
def Home(request):
    cotexto={'home':'active','about':''}
    return render(request,'home.html',cotexto)
    #return HttpResponse('')