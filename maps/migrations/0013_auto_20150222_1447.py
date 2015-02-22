# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0012_auto_20150222_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewgroup',
            name='allow_pdf_uploads',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reviewgroup',
            name='need_url_links',
            field=models.BooleanField(default=True, help_text=b'Should the Reviewer link to the map they reviewed? If they are not uploading a map, they likely should.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='reviewer_email',
            field=models.EmailField(help_text=b'For our records. This will not be shared outside of the partner organisations.', max_length=75, verbose_name=b'Reviewer email address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='map',
            name='url',
            field=models.URLField(help_text=b'Map URL if available', null=True, verbose_name=b'Map URL', blank=True),
            preserve_default=True,
        ),
    ]
