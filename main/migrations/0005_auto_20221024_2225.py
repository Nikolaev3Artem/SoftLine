# Generated by Django 3.1.14 on 2022-10-24 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20221024_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='main.course'),
        ),
    ]
