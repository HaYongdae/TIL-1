from django.contrib import admin

from .models import Board
# Register your models here.

# Admin Page 세부 설정을 위한 클래스
class BoardAdmin(admin.ModelAdmin):
    # DB 데이터 수정할때 순서
    fields = ['content', 'title']
    # DB 데이터 리스트에서 보여질 항목 설정
    list_display = ["title", "updated_at", "created_at"]
    # 우측에 필터링 메뉴 추가
    list_filter = ["updated_at"]
    # DB 리스트에서 검색시 참고할 컬럼 설정
    search_fields = ["title", "content"]

# admin 페이지에 Model과 해당 Model의 설정을 등록하는 부분
admin.site.register(Board, BoardAdmin)
