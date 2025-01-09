from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey('Location',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 verbose_name='Местоположение'
                                 )
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория'
                                 )
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано'
                                       )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено'
                                      )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'


class Category(models.Model):

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано'
                                       )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено'
                                      )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(models.Model):

    name = models.CharField(max_length=256,
                            verbose_name='Название места'
                            )
    is_published = models.BooleanField(default=True,
                                       verbose_name='Опубликовано'
                                       )
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Добавлено'
                                      )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
