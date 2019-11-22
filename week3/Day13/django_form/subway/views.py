from django.shortcuts import render, redirect, get_object_or_404
from .forms import SubwayForm
from .models import Subway
from IPython import embed


# 인덱스는 기존과 동일합니다.
def index(request):
    subways = Subway.objects.all()

    context = {
        'subways':subways
    }
    return render(request, 'subway/index.html', context)

# Form Field를 사용해서 적용함.
def new(request):

    if request.method == "POST":
        # 요청된 데이터를 채운 폼의 인스턴스를 생성
        # form.name = request.POST.get('name') 
        # form.address = request.POST.get('address')
        # .... 한것처럼 요청된 데이터를 넣어줌.
        form = SubwayForm(request.POST)

        # form의 유효성 체크!
        if form.is_valid():
            # 유효성에 문제가 없으면 저장.
            # 모델폼 형식이기에 form.save()를 하면
            # SubwayForm에서 Meta에 설정한 model 로 값이 저장됨.
            subway = form.save()

            # get_absolute_url 을 설정해서 detail 로 간편하게 이동할수 있음.
            return redirect(subway)
    else:
        # 빈 모델폼의 인스턴스를 생성
        # 즉 모델폼에서 설정된 field 만큼 form으로 저장됨.
        form = SubwayForm()
    
    context={
        'form': form
    }
    return render(request, 'subway/form.html', context)

# 디테일 부분 로직은 기존과 동일함
def detail(request, s_id):
    # get_object_or_404 는 모델에서 값을 찾을 수 없을때 404 에러를 발생시켜줌.
    # subway = Subway.objects.get(id=s_id) 동작과 같음. 
    subway = get_object_or_404(Subway, id=s_id)

    context = {
        "subway": subway
    }
    return render(request, 'subway/detail.html', context)

# 삭제 부분 로직은 기존과 동일함
def delete(request, s_id):
    # get_object_or_404 는 모델에서 값을 찾을 수 없을때 404 에러를 발생시켜줌.
    # subway = Subway.objects.get(id=s_id) 동작과 같음. 
    subway = get_object_or_404(Subway, id=s_id)

    if request.method == "POST":
        subway.delete()
    return redirect('subway:index')

def edit(request, s_id):
    subway = get_object_or_404(Subway, id=s_id)

    if request.method == "POST":
        # 요청된 값으로 form을 채우는데 위에서 찾아둔 subway값을 기준으로 수정함.
        # 즉 변경을 하는 subway의 아이디 값을 가지고 있게됨.
        # instance를 설정하지 않으면 아이디값이 비어있게되고 
        # 그 상태에서 save()를 하게 되면 새롭게 db에 생성이 되므로
        # 수정동작이 아닌 생성 동작을 하게 된다.
        form = SubwayForm(request.POST, instance=subway)
        
        # 유효성 검사를 하는 부분
        if form.is_valid():
            sub = form.save()
            return redirect(sub)
    else:
        # 설정된 폼 형태에 찾아둔 subway 정보를 넣는 부분
        # <input type="text" value="{{subway.name}}" name="name">
        # 위와 같이 value에 값을 일일히 넣어주는 불편함이 없어짐.
        # subway.__dict__ 는 값을 Dictionary 형태로 만들어 줌.
        form = SubwayForm(subway.__dict__)
    
    context = {
        'form':form
    }
    return render(request, 'subway/form.html', context)