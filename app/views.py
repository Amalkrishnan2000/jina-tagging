from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'Amal','age':22}
    return render(request,'one.html',d)
