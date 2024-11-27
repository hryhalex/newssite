from django.db import models
from django.urls import reverse
from django.utils.text import slugify 
from unidecode import unidecode
# Create your models here.
# news
# id - INT
# ttitle - Varchar
# content - Text
# created_at - DateTime
# updated_at - DateTime
# photo - Image
# is_published - Boolean

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    content = models.TextField(blank=True, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    objects = models.Manager()


    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})
# метод, который позволяет динамические url-ссылки реализовывать
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-id']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            ascii_title = unidecode(self.title)
            self.slug = slugify(ascii_title)
        super().save(*args, **kwargs)

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


    class Meta: 
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'