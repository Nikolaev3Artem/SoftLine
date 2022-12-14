# Generated by Django 3.1.14 on 2022-10-26 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20221024_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.AddField(
            model_name='course',
            name='rus_price',
            field=models.CharField(default=None, max_length=20, verbose_name='Стоимость курса рубл.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='ua_price',
            field=models.CharField(default=None, max_length=20, verbose_name='Стоимость курса грн.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='usa_price',
            field=models.CharField(default=None, max_length=20, verbose_name='Стоимость курса дол.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=10000, verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='when_end',
            field=models.DateField(verbose_name='Конец курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='when_start',
            field=models.DateField(verbose_name='Начало курса'),
        ),
    ]
