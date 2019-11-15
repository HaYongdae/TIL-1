from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    return render(request, 'crud/index.html', context)

def new(request):
    return render(request, 'crud/new.html')

def create(request):
    article = Article(title=request.POST.get('title'), content=request.POST.get('content'))
    article.save()

    return redirect('/')

def detail(request, id):
    art = Article.objects.get(id=id)

    return render(request, 'crud/detail.html', {'art':art})

def update(request, id):
    art = Article.objects.get(id=id)

    return render(request, 'crud/update.html', {'art':art})

def arti_save(request, id):
    art = Article.objects.get(id=id)

    art.title = request.POST.get('title')
    art.content = request.POST.get('content')

    art.save()

    return redirect(f'/{art.id}/detail/')

def delete(request, id):
    art = Article.objects.get(id=id)

    art.delete()

    return redirect('/')