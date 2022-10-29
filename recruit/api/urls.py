from django.urls import path
from . import views

urlpatterns = [
    path('recruit/', views.RecruitListView.as_view(), name='list'),
    path('recruit/<int:pk>/', views.RecruitDetailView.as_view(), name='detail'),
]