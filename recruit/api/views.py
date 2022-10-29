from rest_framework import generics
from ..models import Recruit
from .serializers import RecruitSerializer


class RecruitListView(generics.ListCreateAPIView):
    serializer_class = RecruitSerializer
    queryset = Recruit.objects.all()
    def get(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        print(slug)
        list = super().list
        self.queryset = Recruit.objects.filter(store__slug=slug)
        return list(request, *args, **kwargs)

class RecruitDetailView(generics.RetrieveDestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer
