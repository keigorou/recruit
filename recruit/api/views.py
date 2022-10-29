from rest_framework import generics
from ..models import Recruit
from .serializers import RecruitSerializer


class RecruitListView(generics.ListCreateAPIView):
    queryset = Recruit.objects.all().order_by('-id')
    serializer_class = RecruitSerializer


class RecruitDetailView(generics.RetrieveDestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer
