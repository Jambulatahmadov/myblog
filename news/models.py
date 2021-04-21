from django.db import models


class MyNews(models.Model):
    title = models.CharField('Название', max_length=150)
    anons = models.CharField('Анонс', max_length=250)
    context = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
