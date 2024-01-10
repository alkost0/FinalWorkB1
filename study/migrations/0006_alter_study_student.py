# Generated by Django 4.2.7 on 2023-11-07 14:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0005_alter_study_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='студент'),
        ),
    ]