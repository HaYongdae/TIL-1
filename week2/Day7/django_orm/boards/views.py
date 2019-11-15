from django.shortcuts import render
from .models import Subway

def index(request):
    return render(request, "boards/index.html")

# subway 작성 폼을 띄우는 함수
def subway_form(request):
    return render(request, "boards/subway.html")

def subway_result(request):
    # form에서 날아오는 POST 값을 받아오는 부분
    name = request.POST.get('name')
    date = request.POST.get('date')
    sandwich = request.POST.get('sandwitch')
    size = request.POST.get('size')
    bread = request.POST.get('bread')
    sauce = request.POST.getlist('source')

    # DB에 저장 되는 부분
    subway = Subway()
    subway.name = name
    subway.date = date
    subway.sandwich = sandwich
    subway.size = size
    subway.bread = bread
    subway.sauce = sauce
    subway.save()

    # DB에 저장된 모든 값을 받아오는 부분
    # QuerySet 형태로 넘어옴. 리스트 형태
    result = Subway.objects.all()

    context = {
        "result": result,
    }

    return render(request, 'boards/result.html', context)

def subway_id(request, id):
    # 하나만 받아오기에 인스턴스 변수가 리턴
    sub = Subway.objects.get(pk=id)
    
    context = {
        "result": sub,
    }

    return render(request, 'boards/sub_id.html', context)