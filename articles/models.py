from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    tags = models.ManyToManyField('Tag', related_name='article', verbose_name='Тематики статьи', through='Scope')


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=60, verbose_name='Название')

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Тематики статьи'

    def __str__(self):
        return str(self.name).capitalize()


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,related_name='scopes')
    is_main = models.BooleanField(default=False, verbose_name='Основной')
