from django.urls import path, include
from . import views

# app_name='diary'

urlpatterns = [
    # # 関数ベースViewの記載
    # path('diary/', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('update/<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
    path('detail/<int:pk>', views.detail, name="detail"),

    # # classベースViewの記載
    path('diary/', views.IndexView.as_view(), name="index"),
    # path('add/', views.AddView.as_view(), name="add"),
    # path('update/<int:pk>', views.UpdateView.as_view(), name="update"),
    # path('delete/<int:pk>', views.DeleteView.as_view(), name="delete"),
    # path('detail/<int:pk>', views.DetailView.as_view(), name="detail"),

]
