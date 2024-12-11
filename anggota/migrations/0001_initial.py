# Generated by Django 5.1.1 on 2024-12-11 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anggota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_anggota', models.CharField(max_length=8)),
                ('nama_anggota', models.TextField()),
                ('alamat_anggota', models.TextField()),
                ('kontak_anggota', models.TextField()),
                ('email_anggota', models.TextField()),
            ],
        ),
    ]
