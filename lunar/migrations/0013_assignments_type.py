# Generated by Django 3.2.8 on 2022-01-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0012_auto_20220130_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignments',
            name='type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
