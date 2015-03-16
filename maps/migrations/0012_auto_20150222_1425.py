# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_auto_20150203_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='reviewer_email',
            field=models.EmailField(default='someone@example.com', max_length=75, verbose_name=b'Reviewer email address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='map',
            name='reviewer_name',
            field=models.CharField(max_length=300, verbose_name=b'Reviewer full name'),
            preserve_default=True,
        ),
    ]
