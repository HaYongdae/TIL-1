from django import forms
from .models import Subway
# 메뉴 구성을 위한 값 미리 설정.
MENU =[
    ('햄', "햄"),
    ('치킨데리야키', '치킨데리야키'),
    ('터키', '터키'),
    ('로스트 치킨', '로스트 치킨'),
    ('스파이시 이탈리안', '스파이시 이탈리안')
]
 
BREAD = [
    ('위트', '위트'),
    ('허니오트','허니오트'),
    ('하티','하티'),
    ('파마산 오레가노','파마산 오레가노'),
]

SAUCE = [
    ('마요네즈','마요네즈'),
    ('스윗 칠리','스윗 칠리'),
    ('사우스 웨스트','사우스 웨스트'),
    ('사우전 아일랜드','사우전 아일랜드'),
]

VEG = [
    ('양상추','양상추'),
    ('피망','피망'),
    ('양파','양파'),
    ('피클','피클'),
    ('올리브','올리브'),
]

DRINK =[
    ('사이다','사이다'),
    ('콜라','콜라'),
    ('환타','환타'),
]

# forms.ModelForm 이 상속됨을 확인! (모델폼 형식으로 폼 필드를 만듬)
class SubwayForm(forms.ModelForm):
    class Meta:
        model = Subway
        # fields = ['name', 'address', 'menu', 
        # 'bread', 'vegetable', 'sauce', 'drink']
        # 모든 필드를 불러오고 싶을때
        fields = '__all__'
        # 해당 부분은 개별 필드마다 input type을 설정하는 부분.
        # choices=[] 설정으로 여러 메뉴를 보여줄 수 있다.
        widgets={
            'menu':forms.Select(choices=MENU), # dropdown 방식
            'bread':forms.RadioSelect(choices=BREAD), # Radio button
            'vegetable':forms.CheckboxSelectMultiple(choices=VEG), # checkbox
            'sauce':forms.CheckboxSelectMultiple(choices=SAUCE),
            'drink':forms.RadioSelect(choices=DRINK)
        }