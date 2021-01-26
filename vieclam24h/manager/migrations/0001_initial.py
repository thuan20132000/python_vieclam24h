# Generated by Django 3.1.5 on 2021-01-26 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='uploads/category/')),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('daft', 'DRAFT'), ('published', 'PUBLISHED')], default='pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='uploads/occupation/')),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('daft', 'DRAFT'), ('published', 'PUBLISHED')], default='pending', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='occupation', to='manager.category')),
            ],
        ),
    ]
