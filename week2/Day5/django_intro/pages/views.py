from django.shortcuts import render
import random
import requests

# Create your views here.
def throw(request):
    return render(request, 'pages/throw.html')

def catch(request):
    # print(request)
    # print(request.path)
    # print(request.method)
    # print(request.META)
    print(request.GET)
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {
        'msg': message,
        'msg2': message2
    }
    return render(request, 'pages/catch.html', context)

def lotto(request):
    return render(request, 'pages/lotto.html')

def lotto_result(request):
    count = int(request.GET.get('count'))
    
    # 다수의 로또 번호를 저장하기 위한 리스트 생성
    lotto_num = []
    for i in range(count):
        lotto_num.append(random.sample(range(1,47),6))
    
    context = {
        'count': count,
        'lotto_num': lotto_num
    }
    return render(request, 'pages/result.html', context)

def artii_form(request):
    return render(request, 'pages/artii_form.html')

def artii_result(request):
    # form 에서 넘어오는 data 
    text = request.GET.get('text')
    
    # 폰트 리스트를 받아와서 리스트로 변환
    f_url = "http://artii.herokuapp.com/fonts_list"
    fonts = requests.get(f_url).text
    fonts = fonts.split('\n')
    
    # 폰트 리스트에서 랜덤으로 하나 뽑기
    font = random.choice(fonts)

    # artii api에 Text 와 font를 넣어 값 요청
    url = f"http://artii.herokuapp.com/make?text={text}&font={font}"
    res = requests.get(url).text

    context = {
        "res":res
    }

    return render(request, 'pages/artii_result.html', context)

def user_new(request):
    return render(request, 'pages/user_new.html')

def user_create(request):
    username = request.POST.get('name')
    pw = request.POST.get('pw')

    context = {
        'username': username,
        'pw': pw
    }

    return render(request, 'pages/user_create.html', context)

def subway_order(request):
    return render(request, 'pages/subway.html')

def subway_result(request):
    name = request.POST.get("name")
    date = request.POST.get("date")
    sandwitch = request.POST.get("sandwitch")
    size = request.POST.get("size")
    bread = request.POST.get("bread")
    # 여러 체크리스트를 받아올땐 getlist
    source = request.POST.getlist("source") 

    context = {
        'name': name,
        'date': date,
        'sandwitch':sandwitch,
        'size': size,
        'bread': bread,
        'source': ", ".join(source)
    }

    return render(request, 'pages/subway_result.html', context)

def static_example(request):
    return render(request, 'pages/static.html')

def index(request):
    return render(request, 'pages/index.html')