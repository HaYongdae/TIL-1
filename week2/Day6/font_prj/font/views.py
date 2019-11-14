from django.shortcuts import render

# Create your views here.
def font(request):
    return render(request, "font/font.html")