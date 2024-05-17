from django.forms import ModelForm
from . import models

# 新規作成用のForm
class DayCreateForm(ModelForm):
    class Meta:
        model = models.Day
        # 以下の記述でDayモデルの全項目を取得
        fields = '__all__'