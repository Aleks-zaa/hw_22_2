from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Contact(models.Model):
    objects = None
    name = models.CharField(max_length=200, verbose_name='Имя')
    email = models.EmailField(verbose_name='почта', unique=True)
    surname = models.CharField(verbose_name='Фамилия')
    contact_img = models.ImageField(upload_to='cars/contact_img', verbose_name='Изображение', **NULLABLE)
    birthday = models.DateField(auto_now_add=True, verbose_name='Дата рождения', **NULLABLE)
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.name} {self.surname} {self.email} {self.birthday}'
