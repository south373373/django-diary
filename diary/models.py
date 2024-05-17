from django.db import models
from django.utils import timezone

# Create your models here.

class Day(models.Model):
    # 主キーを作成しない場合、djangoが自動的に主キーを作成するのが、idのフィールドになる。
    # 作成はしないが内部的には以下の様なデータが自動的に作成される。
    # id = models.AutoField(primary_key=True)
    # 以下の様に独自の主キーを作成する事も可能。
    # title = models.CharField('タイトル', max_length=200, primary_key=True)

    # ()の第1引数を文字列を指定でき、名前 兼 説明。
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self) -> str:
        return self.title