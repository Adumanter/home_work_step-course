from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=200, verbose_name='Имя пользователя')
    user_phone = models.CharField(max_length=200, verbose_name='Номер телефона')
    user_email = models.EmailField(max_length=254, verbose_name='Почта')
    user_comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.user_name