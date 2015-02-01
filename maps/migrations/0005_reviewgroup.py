# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maps', '0004_auto_20150201_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('top_copy', models.TextField(help_text=b'Add HTML here about this set of reviews.')),
                ('name', models.CharField(help_text=b'Friendly name for this grouping (eg. Typhoon Haiyan - Philippines)', max_length=100)),
                ('slug', models.SlugField()),
                ('contact', models.ForeignKey(help_text=b'Admin contact who should deal with data requests.', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(help_text=b'Which event are these reviews for?', to='maps.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
