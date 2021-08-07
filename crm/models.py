from django.db import models

# Create your models here.
class Order(models.Model):
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Номер телефона')
    order_email = models.EmailField(max_length=254, verbose_name='Email')
    order_message = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'