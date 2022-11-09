# Generated by Django 4.1.3 on 2022-11-07 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20221027_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='certification_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Информация об сертификате'),
        ),
        migrations.AddField(
            model_name='course',
            name='certification_uk',
            field=models.CharField(max_length=250, null=True, verbose_name='Информация об сертификате'),
        ),
        migrations.AddField(
            model_name='course',
            name='direction_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Направление курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='direction_uk',
            field=models.CharField(max_length=100, null=True, verbose_name='Направление курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='end_month_en',
            field=models.CharField(choices=[('січня', 'січня'), ('лютого', 'лютого'), ('березня', 'березня'), ('квітня', 'квітня'), ('травня', 'травня'), ('червня', 'червня'), ('липня', 'липня'), ('серпня', 'серпня'), ('вересня', 'вересня'), ('жовтня', 'жовтня'), ('листопада', 'листопада'), ('грудня', 'грудня')], max_length=10, null=True, verbose_name='Конец курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='end_month_uk',
            field=models.CharField(choices=[('січня', 'січня'), ('лютого', 'лютого'), ('березня', 'березня'), ('квітня', 'квітня'), ('травня', 'травня'), ('червня', 'червня'), ('липня', 'липня'), ('серпня', 'серпня'), ('вересня', 'вересня'), ('жовтня', 'жовтня'), ('листопада', 'листопада'), ('грудня', 'грудня')], max_length=10, null=True, verbose_name='Конец курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='language_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Язык программирования'),
        ),
        migrations.AddField(
            model_name='course',
            name='language_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Язык программирования'),
        ),
        migrations.AddField(
            model_name='course',
            name='skill_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Необходимый уровень знаний'),
        ),
        migrations.AddField(
            model_name='course',
            name='skill_uk',
            field=models.CharField(max_length=50, null=True, verbose_name='Необходимый уровень знаний'),
        ),
        migrations.AddField(
            model_name='course',
            name='start_month_en',
            field=models.CharField(choices=[('січня', 'січня'), ('лютого', 'лютого'), ('березня', 'березня'), ('квітня', 'квітня'), ('травня', 'травня'), ('червня', 'червня'), ('липня', 'липня'), ('серпня', 'серпня'), ('вересня', 'вересня'), ('жовтня', 'жовтня'), ('листопада', 'листопада'), ('грудня', 'грудня')], max_length=10, null=True, verbose_name='Месяц начала курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='start_month_uk',
            field=models.CharField(choices=[('січня', 'січня'), ('лютого', 'лютого'), ('березня', 'березня'), ('квітня', 'квітня'), ('травня', 'травня'), ('червня', 'червня'), ('липня', 'липня'), ('серпня', 'серпня'), ('вересня', 'вересня'), ('жовтня', 'жовтня'), ('листопада', 'листопада'), ('грудня', 'грудня')], max_length=10, null=True, verbose_name='Месяц начала курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок курса'),
        ),
        migrations.AddField(
            model_name='course',
            name='title_uk',
            field=models.CharField(max_length=200, null=True, verbose_name='Заголовок курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='request',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
