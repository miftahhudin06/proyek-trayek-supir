# Generated by Django 4.0.5 on 2022-10-20 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0012_alter_laporan_narik_bbm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laporan_narik',
            name='tgl',
            field=models.DateField(null=True),
        ),
    ]
