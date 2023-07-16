# Generated by Django 4.2.2 on 2023-07-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='file',
            field=models.FileField(default='06-06-2023 07:25', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='language',
            field=models.CharField(default='en', max_length=128),
        ),
        migrations.AlterField(
            model_name='experience',
            name='file',
            field=models.FileField(default='06-06-2023 07:25', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='experience',
            name='language',
            field=models.CharField(default='en', max_length=128),
        ),
        migrations.AlterField(
            model_name='manager',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]