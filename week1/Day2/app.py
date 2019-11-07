# render_template : template을 로드하기 위한 모듈
# request : form tag에서 값을 받아 오기 위한 모듈

from flask import Flask, render_template, request
import random
import requests # URL을 요청해서 값을 받아오는 모듈  (pip install requests 필요.)
from pprint import pprint # JSON 타입을 이쁘게 보여주는 모듈

app = Flask(__name__)

# Flask 기본 형태
@app.route('/') # Url 주소 설정하는 부분 
def hello():
    return 'Hello World!' # 해당 String을 페이지에 띄워줌.

@app.route('/mulcam')
def mulcam():
    name = "mulcamp"
    return f'Hello {name}' # f'{name}' : name 이라고 선언된 값이 문자열로 들어감.

@app.route('/greeting/<string:name>') # url 로 전달되는 데이터를 받아옴. <데이터타입:받는 이름>
def greeting(name): # 받는 이름을 인수로 넘겨 받음.
    return f'{name} 님 안녕하세요.'

@app.route('/lunch/<int:num>')
def lunch(num):
    menu = ["짜장면", "짬뽕", "라면", "스파게티", "스테이크", "삼겹살"]
    order = random.sample(menu, num) # sample(Target, 뽑으려는 갯수) Target 은 이터러블 한 값만.
    
    # render_template 사용시 주의 사항!
    # html 등과 같은 template 파일은 templates 라는 폴더안에 저장되어 있어야함. 
    return render_template('menu.html', menu=order) # render_template(template 이름, html로 넘기려는 값)

@app.route('/lotto')
def lotto():
    num = range(1,47) # range(시작값, 끝값) : 시작값<= x <끝값  범위의 숫자를 List 형태로 반환함.
    lotto = random.sample(num, 6)
    return str(lotto)

@app.route('/html')
def html():
    # 문자열을 여러줄로 넣고 싶을때 따옴표 앞뒤로 3개!
    mutiline = '''
    <h1> This is H1 Tag </h1>
    <p> This is P Tag </p>
    '''
    return mutiline

@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', name=name)

@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

@app.route('/send')
def send():
    return render_template('send.html')

@app.route('/receive')
def receive():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('receive.html', name=name, msg=message)

@app.route('/indian')
def indian():
    return render_template('indian.html')

@app.route('/idian_result')
def result():
    list_1 = ['말 많은', '푸른', '어두운', '웅크린', '조용한', '용감한', '지혜로운']
    list_2 = ['늑대', '태양','양', '매', '황소', '불꽃']
    list_3 = ['와 함께 춤을', '의 기상', '은 그림자 속에', '의 환생', '의 죽음', '아래에서', '을 보라', '의 그림자']
    name = request.args.get("name")

    # choice : 1개의 값을 랜덤하게 뽑아내는 역할
    l1 = random.choice(list_1)
    l2 = random.choice(list_2)
    l3 = random.choice(list_3)

    res = f'{name} 의 인디언 네임은 {l1+l2+l3} 입니다.'

    return render_template('result.html', res=res)

@app.route('/lotto_get')
def lotto_get():
    return render_template('lotto_get.html')

@app.route('/lotto_num')
def lotto_num():
    num = request.args.get("num")
    url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}"
    
    # requests: url 을 요청해서 해당 response를 반환함. 
    # .json() json 형식으로 변환하는 부분 (사용전 데이터가 json 형태인것 확인 필요.)

    res = requests.get(url).json()
    
    # List comprehension
    # [ 받는변수 for 받는변수 in 범위로된데이터 ]
    wnum = [ res[f'drwtNo{i}'] for i in range(1,7)]
    
    lotto = random.sample(range(1,47), 6)
    
    # 집합 함수 사용
    match = list(set(wnum) & set(lotto))
    count = len(match)
    msg = ""
    if count == 6:
        msg = "1등입니다."
    elif count == 5:
        msg = "2등입니다."
    elif count == 4:
        msg = "3등입니다."
    elif count == 3:
        msg = "4등입니다."
    else:
        msg = "다음 기회에..."

    return render_template('lotto_result.html', num=num, wnum=wnum, lotto=lotto, msg=msg)


# flask 옵션을 설정하기 위한 구문
if __name__ == "__main__":
    app.run(debug=True, port=8000)