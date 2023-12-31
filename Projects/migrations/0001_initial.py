# Generated by Django 4.2.2 on 2023-06-18 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'Ingilizce'), ('tr', 'Turkce')], default='en', max_length=2)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='static/assets/images/all/')),
                ('country', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'Ingilizce'), ('tr', 'Turkce')], default='en', max_length=2)),
                ('name', models.CharField(max_length=128)),
                ('lastname', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=64)),
                ('image', models.ImageField(upload_to='static/assets/images/all/')),
                ('description', models.TextField()),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Manager',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'Ingilizce'), ('tr', 'Turkce')], default='en', max_length=2)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/assets/images/all/')),
                ('link_project', models.CharField(max_length=128)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='Projects.manager')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'Ingilizce'), ('tr', 'Turkce')], default='en', max_length=2)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='static/assets/images/all/')),
                ('country', models.CharField(max_length=128)),
                ('categoryEducation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.categoryeducation')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
    ]
