import json
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Applicant, Recruit, Store
from .serializers import RecruitSerializer
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


class RecruitListView(generics.ListCreateAPIView):
    serializer_class = RecruitSerializer
    queryset = Recruit.objects.all()
    def get(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        list = super().list
        self.queryset = Recruit.objects.filter(store__slug=slug)
        return list(request, *args, **kwargs)

class RecruitDetailView(generics.RetrieveDestroyAPIView):
    queryset = Recruit.objects.all()
    serializer_class = RecruitSerializer


class PostFormView(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        print(request.body)
        return Response({"message": "Hello, world!"})

@api_view(["POST"])
def post_applicant_data(request):
    data = json.loads(request.body.decode('utf-8'))
    recruit = Recruit.objects.get(id=data["recruit_id"])
    name = data["name"]
    age = data["age"]
    email = data["email"]
    tel = data["tel"]

    applicant = Applicant.objects.create(
        recruit = recruit,
        name = name,
        age = age,
        email = email,
        tel = tel,
    )
    context = { 
            'name': name ,
            'age': age ,
            'email': email ,
            'tel': tel ,
            'recruit': recruit,
            }

    subject = "応募を受け付けました"
    message = render_to_string('recruit/mails/mail.txt', context, request)
    from_email = settings.EMAIL_HOST  # 送信者
    recipient_list = [email]  # 宛先リスト
    send_mail(subject, message, from_email, recipient_list)

    subject = "新着応募がありました"
    message = render_to_string('recruit/mails/mail_admin.txt', context, request)
    from_email = settings.EMAIL_HOST # 送信者
    recipient_list = [recruit.store.email]  # 宛先リスト
    send_mail(subject, message, from_email, recipient_list)

    return Response(status=200)