from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
# forms.pyで作成したformクラスを記載
from . import forms, models
# 汎用Viewで記載する事を想定して追記
from django.views import generic
from django.urls import reverse_lazy


# Create your views here.

# ## 関数Viewの記載
# index画面 → 一覧リストとして表示
# def index(request: HttpRequest) -> HttpResponse:
#     context = {
#         'day_list': models.Day.objects.all(),
#     }
#     return render(request, 'diary/day_list.html', context)

## 汎用View-index
# ListViewはページング処理にも対応可能。
class  IndexView(generic.ListView):
    model=models.Day
    # 以下の記載でページング処理のためのオブジェクトがtemplateへ渡される。
    paginate_by=3


# ## 関数Viewの記載
# 追加画面
def add(request: HttpRequest) -> HttpResponse:
    # context = {
    #     'form': forms.DayCreateForm()
    # }
    # return render(request, 'diary/day_form.html', context)

    # データが送信された際にDBに追加
    # # request.POSTに何かデータがある場合、送信ボタンをクリックして
    # # データが送信された場合はその入力内容をDayCreateFormに入る。
    # # また送信されたデータが空の場合、request.POSTは空なので空の
    # # formが出来上がる。
    form = forms.DayCreateForm(request.POST or None)

    # データが送信されたかの判断をし、更にformの入力内容に不備をチェック。
    # form.is_valid()が失敗した場合は画面上にエラーメッセージを表示。
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form
    }

    return render(request, 'diary/day_form.html', context)

## 汎用View-追加
# class AddView(generic.CreateView):
#     model = models.Day
#     # 使用するformを指定
#     form_class = forms.DayCreateForm
#     success_url = reverse_lazy('index')


# ## 関数Viewの記載
# 編集用
def update(request: HttpRequest, pk: int) -> HttpResponse:
    # 編集対象のページpkがない場合、[Page not found (404)]と表示。
    day = get_object_or_404(models.Day, pk=pk)

    # instance変数に上記で取得したdayモデルのinstanceを指定。こうする事で
    # modelフォームに既にあるDBから取得したデータを紐付ける事が可能。
    # 更新画面の遷移時に既に入力されているデータが埋め込まれた状態で表示。
    form = forms.DayCreateForm(request.POST or None, instance=day)

    # データ送信時にformの入力内容に問題がなければ保存し、indexに遷移。
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('index')
    
    context = {
        'form': form
    }
    # データ送信時にformの入力内容に問題があれば、再度day_form.htmlに遷移。
    return render(request, 'diary/day_form.html', context)

## 汎用View-更新
# class UpdateView(generic.UpdateView):
#     model=models.Day
#     form_class=forms.DayCreateForm
#     success_url=reverse_lazy("index")


# ## 関数Viewの記載
# 削除用
def delete(request: HttpRequest, pk: int) -> HttpResponse:
    # 編集対象のページpkがない場合、[Page not found (404)]と表示。
    day = get_object_or_404(models.Day, pk=pk)

    # データ送信時に対象IDのform自体を削除。
    if request.method == "POST":
        day.delete()
        return redirect('index')
    
    context = {
        'day': day
    }
    # データ送信時にformの削除が実施出来なかった場合、
    # day_confirm_delete.htmlに遷移。
    return render(request, 'diary/day_confirm_delete.html', context)

## 汎用View-削除
# class DeleteView(generic.DeleteView):
#     model=models.Day
#     success_url=reverse_lazy('index')

# ## 関数Viewの記載
# 詳細用(対象IDの個別ごとの詳細)
def detail(request: HttpRequest, pk: int) -> HttpResponse:
    # 編集対象のページpkがない場合、[Page not found (404)]と表示。
    day = get_object_or_404(models.Day, pk=pk)
    
    context = {
        'day': day
    }
    # データ送信時にformの削除が実施出来なかった場合、
    # day_confirm_delete.htmlに遷移。
    return render(request, 'diary/day_detail.html', context)


## 汎用View-詳細
# class DetailView(generic.DetailView):
#     model=models.Day