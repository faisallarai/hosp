# Generated by Django 2.1.7 on 2019-02-21 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0015_auto_20190221_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_new',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='markdown',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='markdown_reason',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='on_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='video_url',
            field=models.URLField(blank=True),
        ),
    ]