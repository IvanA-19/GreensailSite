from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


# Create your models here.
class Teacher(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=250)
    last_name = models.CharField(verbose_name='Фамилия', max_length=250)
    patronymic = models.CharField(verbose_name='Отчество', max_length=250)
    bio = models.CharField(verbose_name='ФИО', max_length=250)
    about = models.TextField(verbose_name='О педагоге')
    photo = models.ImageField(upload_to='media/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Педагог'
        verbose_name_plural = 'Педагоги'

    def __str__(self):
        return self.bio


class Mugs(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    description = models.TextField(verbose_name='Описание')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Педагог')
    link_for_recording = models.TextField(verbose_name='Ссылка для записи')
    preview = models.ImageField(verbose_name='Главное фото', upload_to='media/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кружок'
        verbose_name_plural = 'Кружки'


class MugsPhotos(models.Model):
    mug = models.ForeignKey(Mugs, on_delete=models.CASCADE, verbose_name='Кружок')
    photo = models.ImageField(verbose_name='Фото', upload_to='media/', null=True)

    class Meta:
        verbose_name_plural = 'Фото с кружков'


class Contests(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    link = models.CharField(max_length=250, verbose_name='Ссылка на форму')
    photo = models.ImageField(verbose_name='Фото', upload_to='media/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Конкурс'
        verbose_name_plural = 'Конкурсы'


class Masterclasses(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    link = models.CharField(max_length=250, verbose_name='Ссылка на форму')
    photo = models.ImageField(verbose_name='Фото', upload_to='media/', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Мастер-класс'
        verbose_name_plural = 'Мастер-классы'
