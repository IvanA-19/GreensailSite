# Generated by Django 5.0 on 2023-12-27 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_actualevents_actual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('div_id', models.CharField(max_length=250)),
                ('post_id', models.IntegerField()),
                ('owner_id', models.IntegerField()),
                ('hash', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Актуальные события',
            },
        ),
        migrations.DeleteModel(
            name='Actual',
        ),
    ]
