from django.db import models
from django.urls import reverse

class Subway(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    menu = models.CharField(max_length=10)
    bread = models.CharField(max_length=10)
    vegetable = models.CharField(max_length=30)
    sauce = models.CharField(max_length=50)
    drink = models.CharField(max_length=10)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # 해당 인스턴스가 불려올때 pk 값을 받아 설정된 path로 보냄.
    def get_absolute_url(self):
        return reverse("subway:detail", kwargs={"s_id": self.pk})
    