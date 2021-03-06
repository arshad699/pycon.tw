# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_remove_out_of_place_help_texts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoredevent',
            name='category',
            field=models.CharField(choices=[('PRAC', 'Best Practices & Patterns'), ('COM', 'Community'), ('DB', 'Databases'), ('DATA', 'Data Analysis'), ('EDU', 'Education'), ('EMBED', 'Embedded Systems'), ('FIN', 'FinTech'), ('GAME', 'Gaming'), ('GRAPH', 'Graphics'), ('OTHER', 'Other'), ('CORE', 'Python Core (language, stdlib, etc.)'), ('INTNL', 'Python Internals'), ('LIBS', 'Python Libraries'), ('SCI', 'Science'), ('SEC', 'Security'), ('ADMIN', 'Systems Administration'), ('TEST', 'Testing'), ('WEB', 'Web Frameworks')], max_length=5, verbose_name='category'),
        ),
    ]
