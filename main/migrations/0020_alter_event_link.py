# Generated by Django 5.0 on 2024-01-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_event_options_event_link_alter_event_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(max_length=300, verbose_name='Ссылка "подробнее"'),
        ),
    ]
