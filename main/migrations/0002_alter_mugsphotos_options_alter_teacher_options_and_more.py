# Generated by Django 5.0 on 2023-12-25 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mugsphotos',
            options={'verbose_name_plural': 'Фото с кружков'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': 'Педагоги'},
        ),
        migrations.AlterField(
            model_name='mugsphotos',
            name='photo',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.CharField(max_length=250),
        ),
    ]
