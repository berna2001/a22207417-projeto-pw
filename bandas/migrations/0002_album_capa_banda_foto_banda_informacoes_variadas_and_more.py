# Generated by Django 4.0.6 on 2024-04-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, upload_to='album_capas/'),
        ),
        migrations.AddField(
            model_name='banda',
            name='foto',
            field=models.ImageField(blank=True, upload_to='bandas_fotos/'),
        ),
        migrations.AddField(
            model_name='banda',
            name='informacoes_variadas',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='link_spotify',
            field=models.URLField(blank=True),
        ),
    ]
