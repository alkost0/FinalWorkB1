# Generated by Django 4.2.7 on 2023-11-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0002_alter_students_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='student',
            field=models.ManyToManyField(blank=True, null=True, to='study.students', verbose_name='студент'),
        ),
    ]