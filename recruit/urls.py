from django.urls import path
from . import views

urlpatterns = [
    path('recruit/home/<slug:slug>', views.IndexView.as_view(), name='index')
]