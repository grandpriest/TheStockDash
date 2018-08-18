from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('1/',views.testing,name='testing'),
    path('1/update/',views.update,name="update"),
    path('update1/', views.update1, name="update1"),
]