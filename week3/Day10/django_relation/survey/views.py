from django.shortcuts import render, redirect
from .models import Question, Choice

# 모든 설문 내용을 가져와서 보여줌.
def index(request):
    questions = Question.objects.all()
    context = {
        "questions": questions
    }
    return render(request, 'survey/index.html', context)

# 새로운 질문 내용을 저장하기 위한 부분
def new(request):

    # POST 방식으로 접근할때만 DB에 저장동작.
    if request.method == "POST":
        q = request.POST.get('question')
        question = Question()
        question.question = q
        question.save()
        return redirect('survey:index')
    # GET 방식으로 오는 경우 폼을 보여줌.
    return render(request, 'survey/new.html')

# 질문에 세부 사항을 나타내는 곳.
def detail(request, q_id):
    # 부모 테이블 정보를 가져옴.
    question = Question.objects.get(id=q_id)

    # 질문에 대한 세부 내용을 불러오는 곳
    # 여기서 포인트는 (자식테이블명_set)
    # 부모 테이블이 가진 모든 자식테이블을 불러옴.
    surveys = question.choice_set.all()
    context = {
        'question': question,
        'surveys': surveys
    }
    return render(request, 'survey/detail.html', context)

# 부모 테이블 내용을 수정하는 곳
def edit(request, q_id):
    # 부모 테이블 정보를 가져옴. 
    q = Question.objects.get(id=q_id)

    # POST 방식일때만 수정 내용 저장.
    if request.method == "POST":
        text = request.POST.get('question')
        q.question = text
        q.save()
        return redirect('survey:detail', q.id)
    else:
        context = {
            "question":q
        }
        return render(request, 'survey/edit.html', context)

# 부모 테이블 삭제를 위한 부분
def delete(request, q_id):
    q = Question.objects.get(id=q_id)

    # 데이터 삭제 동장은 GET방식이 아닌 POST로!
    # GET 방식은 데이터 정보를 요청할때 사용함.
    if request.method == "POST":
        q.delete()
    
    return redirect('survey:index')

# 설문 항목을 저장하기 위한 곳!
def survey(request, q_id):
    # 부모 데이터 정보를 가져옴.
    question = Question.objects.get(id=q_id)

    # POST 방식일때만 저장
    if request.method == "POST":
        text = request.POST.get("survey")
        # 자식 데이터 저장을 위한 인스턴스 생성
        s = Choice()
        s.survey = text
        s.question = question # 부모테이블 저장.FK 이기 때문에 필수
        s.save()
    
    return redirect('survey:detail', question.id)

# 설문 항목을 수정하는 곳
def survey_edit(request, c_id):
    # 설문(자식) 데이터를 가져오는 부분
    survey = Choice.objects.get(id=c_id)

    # print(f'survey_edit method is {request.method}')
    # POST 방식일 때만 수정가능 하게
    if request.method == "POST":
        text = request.POST.get('survey')
        survey.survey = text
        survey.save()
        # 이미 부모정보는 저장이 되어 있기에 수정 부분만 저장해주면 됨.
        # 자식 인스턴스에서 부모의 정보를 가져오기 위해서는 
        return redirect('survey:detail', survey.question_id)
    else:
        # GET 방식일때는 폼을 보여줌.
        context = {
            "survey": survey
        }
        return render(request, 'survey/sur_edit.html', context)

# 설문 항목 삭제하는 부분
def survey_del(request, c_id):
    survey = Choice.objects.get(id=c_id)

    # 데이터를 직접 변경하기에 POST 일때만 동작하게!
    if request.method == "POST":
        survey.delete()
    
    return redirect('survey:detail', survey.question_id)

# 설문 항목에서 투표하기를 눌렀을때 처리 하는 곳
def vote(request, c_id):
    survey = Choice.objects.get(id=c_id)

    # print(f'vote method is {request.method}')
    # 데이터를 직접 변경하기에 POST 일 때만 동작!
    if request.method == "POST":
        survey.votes += 1
        survey.save()

    return redirect('survey:detail', survey.question_id)