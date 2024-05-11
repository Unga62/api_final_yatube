from django.contrib.auth import get_user_model
from django.db import models

from api.const import TEXT_SLICE

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя группы')
    slug = models.SlugField(
        unique=True,
        verbose_name='Cокращенное имя группы'
    )
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title[:TEXT_SLICE]


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:TEXT_SLICE]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True
    )

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return f'{self.post}, {self.author}, {self.text[:TEXT_SLICE]}'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )

    def __str__(self):
        return f'Подписчики: {self.user}; Подписки: {self.following}'
