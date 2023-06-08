from django.shortcuts import render

# Create your views here.
def videoCall(request):
    return render(request,"videoCall/public/index.html")
