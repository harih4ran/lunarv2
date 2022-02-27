# Generated by Django 3.2.8 on 2022-02-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunar', '0016_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='college',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='course',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='first_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='profile_photo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='student_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='hero',
            name='year_of_enrollment',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]