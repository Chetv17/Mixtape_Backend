# Generated by Django 4.1.4 on 2023-01-05 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=75, unique=True)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
    ]