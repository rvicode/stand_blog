from django.db import models


class ContactUs(models.Model):
    username = models.CharField(max_length=30, verbose_name='نام کاربری')
    email = models.EmailField(verbose_name='ایمیل')
    number = models.CharField(max_length=13, verbose_name='شماره تلفن')
    subject = models.CharField(max_length=40, verbose_name='موضوع')
    massage = models.TextField(verbose_name='پیغام')

    def __str__(self):
        return f'{self.username} : {self.subject}'

    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'ارتباطات'

