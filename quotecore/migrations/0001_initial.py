# Generated by Django 5.1.1 on 2024-10-01 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=128, verbose_name='Last Name')),
                ('pseudonym', models.CharField(max_length=128, verbose_name='Pseudonym')),
                ('birth_date', models.DateTimeField(verbose_name='Birth Date')),
                ('death_date', models.DateTimeField(blank=True, verbose_name='Death Date')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, verbose_name='Label')),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=256, verbose_name='Source')),
                ('text', models.CharField(max_length=1024, verbose_name='Text')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='quotecore.author', verbose_name='quotes')),
                ('category', models.ManyToManyField(to='quotecore.category')),
            ],
        ),
    ]