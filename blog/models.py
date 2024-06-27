from django.db import models


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=100, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='cars/image', blank=True, null=True, verbose_name='Изображение')
    public = models.IntegerField(verbose_name='признак публикации', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.CharField(max_length=100, verbose_name='slug', blank=True, null=True)

    view_counter = models.PositiveIntegerField(
        verbose_name='Счетчик просмотров',
        help_text='Укажите колличество просмотров',
        default=0
    )

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return f'{self.title} {self.description} {self.public} {self.created_at}'
