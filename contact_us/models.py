from django.db import models


class ContactUs(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    number = models.CharField(max_length=13)
    subject = models.CharField(max_length=40)
    massage = models.TextField()

    def __str__(self):
        return f'{self.username} : {self.subject}'
