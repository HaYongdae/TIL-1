from flask import Flask, render_template, request
import requests
from decouple import config # .env 파일에 저장된 Token 받아오는 라이브러리
from pprint import pprint
import random

app = Flask(__name__)

token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"

@app.route('/telegram')
def telegram():
    # 토큰값을 받아오자
    # token = config('TOKEN')
    # telegram bot api 문서에 request url
    #  >> https://api.telegram.org/bot<token>/METHOD_NAME
    # base_url = f"https://api.telegram.org/bot{token}"

    # telegram 서버에 data 요청
    # .json() 이 없으면 응답코드만 받음
    res = requests.get(f'{base_url}/getUpdates').json()
    
    # chat id 추출 (sendMessage 할 때 필요하기 때문)
    chat_id = res['result'][0]['message']['chat']['id']
    
    lotto = random.sample(range(1,47),6)
    
    send_url = f'/sendMessage?chat_id={chat_id}&text={lotto}'

    res = requests.get(base_url+send_url).json()

    pprint(res)
    return ''

# chat form 을 불러오는 부분
@app.route('/chat')
def chat():
    return render_template('chat.html')

# chat.html 에서 입력된 data 를 받아서 텔레그램으로 보내는 부분
@app.route('/send_msg')
def send_message():
    # form 에서 chat라는 이름의 데이터를 받아오는 곳.
    req = request.args.get("chat")

    # chat_id 값을 받아오기 위해 사용된 2줄
    res = requests.get(f'{base_url}/getUpdates').json()
    chat_id = res['result'][0]['message']['chat']['id']

    # telegram 에 메세지를 보내기 위한 url
    send_url = f'/sendMessage?chat_id={chat_id}&text={req}'
    response = requests.get(base_url+send_url)

    return "보내기 완료."

# telegram webhook 서버가 보낸 데이터를 받는곳
#   - set_webhook.py 에서 root 주소에 받기로 설정함.
@app.route('/', methods=['POST'])
def tel_web():
    # 네이버 개발자 센터에서 받은 Client_id / Client_secret
    C_ID = config('C_ID')
    C_SC = config('C_SC')
    # 파파고 요청 header
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": C_ID,
        "X-Naver-Client-Secret": C_SC
    }
    # 파파고 요청 url 
    url = "https://openapi.naver.com/v1/papago/n2mt"

    # 텔레그램에서 보낸 json에서 messag 부분만 가져옴.
    req = request.get_json().get('message')
    
    # req 가 비어있는지 확인.
    if req is not None:
        # sendMessage에서 필요한 chat_id 획득!
        # 텔레그램에서 보낸 text 가져옴.
        chat_id = req.get('chat').get('id')
        text = req.get('text')

    # 텔레그램에서 받은 text를 가지고 동작 분류
    if "로또" in text:
        msg = random.sample(range(1,47), 6)

    elif "/번역" in text:
        #"/번역 내용" 으로 메세지가 입력되기에
        # 내용만 남게 replace 함.
        re_txt = text.replace("/번역", "")
        # 파파고에서 필요한 data 파일
        data = {
            "source": "ko",
            "target": "en",
            "text": re_txt
        }
        # 파파고에 설정된 데이터를 보내서 결과를 요청함.
        res = requests.post(url, headers=headers, data=data).json()
        # 결과값을 msg 에 넣음.
        msg = res.get('message').get('result').get('translatedText')

    else:
        # 받은 텍스트를 되돌려주는 메아리 부분
        msg = text
       
    # 텔레그램에 메세지를 날리는 부분
    send_url = f'/sendMessage?chat_id={chat_id}&text={msg}'
    res = requests.get(base_url+send_url)

    # return <body>, <status code> 로 구성
    # 200 리턴이 올때까지 텔레그램 서버에서 계속 데이터 보냄
    return '', 200

# papago 동작 확인을 위한 부분.
@app.route('/papago')
def papago():
    C_ID = config('C_ID')
    C_SC = config('C_SC')
    url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": C_ID,
        "X-Naver-Client-Secret": C_SC
    }

    data = {
        "source": "ko",
        "target": "en",
        "text": "안녕하세요."
    }

    req = requests.post(url, headers=headers, data=data).json()

    print(req)

    return "Finish!"


# flask 설정하는 부분.
if __name__ == "__main__":
    app.run(debug=True)