# Generated by Django 5.0 on 2024-01-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medapp', '0002_profile_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='medicine_images/')),
                ('expire_date', models.DateField()),
            ],
        ),
    ]
