from django.db import models

# 클래스 명은 테이블명
class Board(models.Model):
    # 변수명은 컬럼명
    title = models.CharField(max_length=10)
    content = models.TextField()
    # auto_now_add : 데이터가 새로 생성될때 날짜시간 자동 추가
    # auto_now : 데이터가 수정될때 날짜시간 자동 추가
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Board 테이블에 어떤 데이터가 들었는지 확인하기 위해 문자열로 넘기는 부분
    # 해당 객체를 부르면 __str__ 에서 정해진 리턴값을 던져줌.
    # 설정하지 않으면 <Board: Board object (2)> 형식으로 어떤 데이터가 들어있는지 알수 없다.
    def __str__(self):
        return f'{self.title}'


class Subway(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField()
    sandwich = models.CharField(max_length=20)
    size = models.IntegerField()
    bread = models.CharField(max_length=20)
    sauce = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} : {self.bread} ({self.date})'
