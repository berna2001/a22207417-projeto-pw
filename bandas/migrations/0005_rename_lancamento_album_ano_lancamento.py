# Generated by Django 4.0.6 on 2024-04-20 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0004_banda_nacionalidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='lancamento',
            new_name='ano_lancamento',
        ),
    ]
