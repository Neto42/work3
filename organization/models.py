from django.db import models

from base.models import BaseModel


class Organization(BaseModel):
    organization = models.CharField(
        verbose_name='Организация',
        max_length=50,
    )

    inn = models.BigIntegerField(
        verbose_name='ИНН',
        unique=True,
    )

    kpp = models.IntegerField(
        verbose_name='КПП',
        unique=True,
    )

    ogrn = models.BigIntegerField(
        verbose_name='ОГРН',
        unique=True,
    )

    image = models.ImageField(verbose_name='Логотип организации', null=True, blank=True)
    text_org = models.TextField(verbose_name='Описание организации')
    link = models.CharField(verbose_name='Ссылка на сайт организации', max_length=50, null=True, blank=True)
    email = models.EmailField(verbose_name='Почта организации')

    class Meta:
        db_table = 'organization'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return f"{self.organization}"
