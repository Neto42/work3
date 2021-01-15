from django.db import models
from django.urls import reverse

from base.models import BaseModel
from organization.models import Organization
from user.models import Profile


class Work(BaseModel):
    work = models.CharField(
        verbose_name='работа',
        max_length=20,
        unique=True
    )

    class Meta:
        db_table = 'work'
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['work']

    def __str__(self):
        return f"{self.work}"


class Ad(BaseModel):
    user = models.ForeignKey(
        Profile,
        verbose_name='пользователь',
        on_delete=models.CASCADE,
    )

    work = models.ForeignKey(
        Work,
        verbose_name='работа',
        on_delete=models.CASCADE
    )

    organization = models.ForeignKey(
        Organization,
        verbose_name='организация',
        on_delete=models.CASCADE
    )

    ad_text = models.TextField(verbose_name='Текст объявления')
    salary = models.IntegerField(verbose_name='Заработная плата', default='0')

    class Meta:
        db_table = 'ad'
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ["organization"]

    def __str__(self):
        return f"{str(self.organization)}"

    def get_absolute_url(self):
        return reverse('ad-detail', args=[str(self.id)])