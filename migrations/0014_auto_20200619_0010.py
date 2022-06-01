# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-06-18 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agrotrade', '0013_producegroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='producegroup',
            name='name',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bidtag',
            name='tag',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='farmerasks',
            name='contact_number',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='farmerasks',
            name='medium',
            field=models.TextField(choices=[('Web', 'Web'), ('CC', 'Call Center'), ('SMS', 'SMS')], editable=False),
        ),
        migrations.AlterField(
            model_name='language',
            name='language',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='display_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='display_name_en_us',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='display_name_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='display_name_lug',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='display_name_luo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='display_name_run',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='image_path',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='producedefinition',
            name='produce_name',
            field=models.TextField(blank=True, max_length=50, null=True, verbose_name='Produce name'),
        ),
        migrations.AlterField(
            model_name='traderbids',
            name='contact_number',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='traderbids',
            name='medium',
            field=models.TextField(choices=[('Web', 'Web'), ('CC', 'Call Center'), ('SMS', 'SMS')], editable=False),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='code',
            field=models.TextField(unique=True, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='code_en_us',
            field=models.TextField(null=True, unique=True, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='code_es',
            field=models.TextField(null=True, unique=True, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='code_lug',
            field=models.TextField(null=True, unique=True, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='code_luo',
            field=models.TextField(null=True, unique=True, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='code_run',
            field=models.TextField(null=True, unique=True, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='unit_name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='unit_name_en_us',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='unit_name_es',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='unit_name_lug',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='unit_name_luo',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='unitsdefinition',
            name='unit_name_run',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='language',
            field=models.TextField(choices=[('en-us', 'English'), ('lug', 'Luganda'), ('luo', 'Luo'), ('run', 'Runyakitara'), ('es', 'Spanish')], default='en-us'),
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='message',
            field=models.TextField(blank=True, help_text='The incoming SMS'),
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='status',
            field=models.TextField(choices=[('Rev', 'Reviewed'), ('Uns', 'Unseen')], default='Uns'),
        ),
        migrations.AlterField(
            model_name='verification',
            name='code',
            field=models.TextField(),
        ),
    ]
