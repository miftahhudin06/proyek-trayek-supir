# Generated by Django 4.0.5 on 2022-09-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_rename_profile_profil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=100, null=True)),
                ('nama', models.CharField(max_length=100, null=True)),
                ('tgl_lahir', models.DateField()),
                ('jadwal', models.CharField(max_length=100, null=True)),
                ('alamat', models.CharField(max_length=200, null=True)),
                ('avatar', models.ImageField(upload_to='supir_img')),
            ],
        ),
    ]