# Generated by Django 4.1.4 on 2023-01-03 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('playlists_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('cover', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('playlist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='playlists_api.playlist')),
            ],
        ),
    ]
