# Generated by Django 4.0.6 on 2024-03-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_nome', models.CharField(max_length=50)),
                ('ultimo_nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
                ('indentificacao', models.CharField(max_length=50)),
            ],
        ),
    ]
