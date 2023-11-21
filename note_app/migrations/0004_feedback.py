# Generated by Django 4.2.4 on 2023-11-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_app', '0003_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('msg', models.TextField()),
            ],
        ),
    ]
