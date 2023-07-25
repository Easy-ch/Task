from django.db import models

# Create your models here.
class OnlineShop(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10,decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Отметьте, уместен ли торг')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.id} {self.title} {self.price}'
    class Meta:
        db_table = 'advertisements'

      



