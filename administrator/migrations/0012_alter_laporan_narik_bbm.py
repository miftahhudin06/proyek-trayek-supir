# Generated by Django 4.0.5 on 2022-10-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0011_laporan_narik_tgl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporan_narik',
            name='bbm',
            field=models.PositiveIntegerField(default=1500000),
        ),
    ]
