from decouple import config
import requests
from pprint import pprint

token = config('TOKEN')
base_url = f"https://api.telegram.org/bot{token}"
# url = "f8d316c1.ngrok.io"
# 해당 URL에 telegram webhook 서버가 데이터를 보내줌.
url = "mulcamped.pythonanywhere.com"

# webhook 요청 주소를 만드는 부분
setweb_url = f'/setWebhook?url={url}'

# setwebhook 요청을 보내는 부분.
req = requests.get(base_url+setweb_url).json()

# 결과값 확인
# Webhook was set. <- 메세지 확인!
pprint(req)
