from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name='Имя',
        on_delete=models.CASCADE
    )

    ADMIN = '1'
    MODERATOR = '2'
    USER = '0'

    STATUS = (
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    )
    status = models.CharField(
        verbose_name='Статус пользователя',
        max_length=10,
        choices=STATUS
    )
    image = models.ImageField(verbose_name='Фотография пользователя', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["status"]

    def __str__(self):
        return f"{str(self.user)}"


@receiver(post_save, sender=User)
def created_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

