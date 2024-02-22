from django.db import models
from django.urls import reverse

# Create your models here.
class ReasonToVisit(models.Model):
    name = models.CharField(max_length=250, verbose_name='عنوان')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('reason', args=[self.id])

    class Meta:
        verbose_name = 'دلیل مراجعه'
        verbose_name_plural = 'دلایل مراجعه'


class Person(models.Model):
    first_name = models.CharField(max_length=250, verbose_name='نام')
    last_name = models.CharField(max_length=250, verbose_name='نام خانوادگی')
    phone_number = models.CharField(max_length=100, verbose_name='تلفن همراه')
    address = models.TextField(blank=True, null=True, verbose_name='آدرس')
    reasons_to_visit = models.ManyToManyField(ReasonToVisit, related_name='people', verbose_name='دلایل مراجعه')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse('person', args=[self.id])
    
    class Meta:
        verbose_name = 'مراجع'
        verbose_name_plural = 'مراجعین'