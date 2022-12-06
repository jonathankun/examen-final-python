# Generated by Django 4.1.3 on 2022-12-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('dni', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Mesero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('procedencia', models.CharField(default='', max_length=40)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('precio', models.CharField(max_length=20)),
                ('procedencia', models.CharField(default='', max_length=40)),
            ],
        ),
    ]
