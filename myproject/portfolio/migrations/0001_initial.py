# Generated by Django 3.0.3 on 2020-03-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.TextField()),
                ('end_year', models.TextField()),
                ('position', models.TextField()),
                ('desc', models.TextField()),
            ],
        ),
    ]