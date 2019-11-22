from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm#, AuthorForm
from IPython import embed

def index(request):
    articles = Article.objects.all()
    context = {
        "articles": articles
    }
    return render(request, 'article/index.html', context)


def new(request):
    if request.method == "POST":
        # 기존에 처리 했던 방식!
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # article = Article()
        # article.title = title
        # article.content = content
        
        # 폼 필드를 설정해서 한줄에 해결!
        # form = ArticleForm(request.POST)
        
        # 유효성 검사 이상없으면 True
        if form.is_valid(): 
            # 기존에 했었던 방식
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title=title, content=content)
            author = form.save()
            # embed() # 해당 라인에서 궁금한 값들을 디버깅을 하기 위해 추가
            return redirect('article:index')
    else:
        form = ArticleForm()

    # 폼의 인스턴스를 context에 담아서 html로 보낸다.
    # 그러면 django에서 알아서 인스턴스를 참고하여 
    # 필요한 input tag들을 만들어 준다.
    context = {
        "form": form
    }
    return render(request, 'article/new.html', context)

def detail(request, a_id):
    # a_id 로 찾을때 값이 없으면 500 (서버에러)가 나타나는데
    # 찾을수 없는 범위이기에 404에러가 발생하는게 맞음.
    # get_object_or_404 는 값이 없을때 알아서 404 에러 발생해줌.
    # article = Article.objects.get(id=a_id)
    article = get_object_or_404(Article, id=a_id)

    context = {
        "article": article
    }
    return render(request, 'article/detail.html', context)

def edit(request, a_id):
    # article = Article.objects.get(id=a_id)
    article = get_object_or_404(Article, id=a_id)

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 일반 폼 필드로 저장할때는 해당 방법으로 시도할 수 있음.
            # form.cleaned_data 는 form 필드에 들어 있는 내용을 dictionary 형태로 만들어 줌.
            article.title = form.cleaned_data.get('title')
            article.content = form.cleaned_data.get('content')
            article.save()
            return redirect(article)
    else:
        # 읽어온 article 값을 폼 필드에 넣어 폼을 생성.
        form = ArticleForm(initial=article.__dict__)
        # embed()
    
    context = {
        'form': form
    }
    return render(request, 'article/new.html', context)

def delete(request, a_id):
    article = Article.objects.get(id=a_id)
    if request.method == "POST":
        article.delete()
    
    return redirect('article:index')