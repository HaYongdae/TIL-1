from django.shortcuts import render
from django.http import HttpResponse # Text를 보낼때 사용
import random
from faker import Faker
from datetime import datetime


def index(request):
    return render(request, 'index.html')

def profile(request, name, age):
    list_1 = ['말 많은', '푸른', '어두운', '웅크린', '조용한', '용감한', '지혜로운']
    list_2 = ['늑대', '태양','양', '매', '황소', '불꽃']
    list_3 = ['와 함께 춤을', '의 기상', '은 그림자 속에', '의 환생', '의 죽음', '아래에서', '을 보라', '의 그림자']
    
    i_name = random.choice(list_1)+random.choice(list_2)+random.choice(list_3)
    
    lotto = random.sample(range(1,47), 6)
    lotto.sort()
    # list comprehension
    l_num=[ str(l) for l in lotto ]
    
    context = {
        'name': name,
        'age': age,
        'i_name': i_name,
        'lotto' : ", ".join(l_num)
    }

    return render(request, 'profile.html', context)

def age(request, age):
    context = {
        'age': age
        }
    return render(request, 'age.html', context)

def square(request, num):
    context = {
        'res': num**2
    }
    return render(request, 'squ.html', context)

def plus(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'res': num1+num2
    }
    return render(request, 'plus.html', context)

def minus(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'res': num1-num2
    }
    return render(request, 'minus.html', context)

def multi(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'res': num1*num2
    }
    return render(request, 'multi.html', context)

def divid(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'res': num1/num2
    }
    return render(request, 'divid.html', context)

def job(request, name):
    fake = Faker('ko_KR')
    job = fake.job()

    context = {
        'name': name,
        'job': job
    }

    return render(request, 'job.html', context)

def image(request):
    num = random.choice(range(1, 100))
    url = f"https://picsum.photos/id/{num}/200/300"

    context = {
        'url': url
    }

    return render(request,'image.html', context)

def dtl(request):
    foods = ["짜장면", "탕수육", "짬뽕", "양장피", "군만두", "고추잡채", "볶음밥"]
    my_sentence = 'life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now() #현재 시간
    empty_list = []

    context = {
        "foods": foods,
        "my_sentence": my_sentence,
        "messages": messages,
        "timenow" : datetimenow,
        "empty_list": empty_list,
    }

    return render(request, 'dtl.html', context)

def birth(request):
    today = datetime.now()
    
    if today.month == 7 and today.date == 22:
        res = True
    else:
        res = False
    
    birth = datetime(2020, 7, 22)
    d_day = (today-birth).days

    context = {
        'result': res,
        'd_day': d_day
    }
    return render(request, 'birth.html', context)
