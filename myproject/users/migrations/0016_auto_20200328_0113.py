# Generated by Django 3.0.4 on 2020-03-28 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200328_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='award_place',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='college_end_month_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='college_start_month_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_end_month_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_start_month_year',
            field=models.DateField(),
        ),
    ]
