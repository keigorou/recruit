from email.policy import default
from tkinter import image_names
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='店舗名', max_length=50)
    slug = models.SlugField(unique=True)
    email = models.EmailField(verbose_name='メールアドレス')
    email_2 = models.EmailField(verbose_name='メールアドレス', default="")

    def __str__(self) -> str:
        return self.name

class Recruit(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    recruitment_type = models.CharField(verbose_name='職種', max_length=50, blank=True)
    hourlywage = models.CharField(verbose_name='給与', max_length=50)
    worktime = models.CharField(verbose_name='勤務時間', max_length=50, blank=True)
    description = models.TextField(verbose_name='詳細', blank=True)
    publish = models.BooleanField(verbose_name='公開する', default=True)


    def __str__(self) -> str:
        return self.store.name

class Applicant(models.Model):
    GENDER_CHOICES = (
        ('1', '女性'),
        ('2', '男性'),
        ('3', 'その他'),
    )
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名前', max_length=50)
    age = models.IntegerField(verbose_name='年齢')
    gender = models.CharField(verbose_name='性別', choices=GENDER_CHOICES, max_length=2, default=3)
    email = models.EmailField(verbose_name='メールアドレス')
    tel = models.CharField(verbose_name='電話番号', max_length=20)

    def __str__(self) -> str:
        return self.name
    
