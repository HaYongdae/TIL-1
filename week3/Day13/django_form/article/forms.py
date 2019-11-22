from django import forms
# from .models import Author

CHECK_BOX = [
    ('one', "하나"),
    ('two', "둘"),
    ('three', "셋")
]
MONTH_EN = {
    1:('JAN'), 2:('FEB'), 3:('MAR'), 4:('APR'),
    5:('MAY'), 6:('JUN'), 7:('JUL'), 8:('AUG'),
    9:('SEP'), 10:('OCT'), 11:('NOV'),12:('DEC')
}
# 일반 폼 필드 생성 방법
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # input tag 안에 attribute 설정을 하는 방법
    # 1. widget을 설정하고 안에 attrs를 넣는 방법
    #
    # title = forms.CharField(
    #     #위젯을 설정하고 안에 attrs = {dict} 형식으로
    #     widget=forms.TextInput(
    #         attrs={'class':"form-control"}
    #         )
    # )
    # content = forms.CharField(
    #     max_length=5, 
    #     widget= forms.Textarea(
    #         attrs={
    #             'class':'form-control',
    #             'placeholder':"5자리만!!!"
    #             }
    #         )
    #     )
    
    #
    # 2. 해당 form 클래스의 메소드로 __init__으로 설정하는 방법
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['content'].widget.attrs.update({'class': 'def'})

    # 체크 박스 사용
    # content = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=CHECK_BOX
    # )

    #라디오 버튼
    # content = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     choices=CHECK_BOX
    # )

    # 드랍다운 방식
    # content = forms.ChoiceField(
    #     widget=forms.Select,
    #     choices=CHECK_BOX
    # )

    # 날짜
    # content = forms.DateField(
    #     widget= forms.SelectDateWidget(
    #         years=range(1990, 2020),
    #         months=MONTH_EN
    #     )        
    # )

# 모델 폼으로 폼 생성하는 방법
# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ['name','company']