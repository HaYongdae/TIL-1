from django.shortcuts import render

# Create your views here.
def google_font(request):
    return render(request, 'font/font.html')