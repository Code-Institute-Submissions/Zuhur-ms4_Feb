# Generated by Django 3.2.5 on 2021-12-16 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0002_auto_20211216_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchandise',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='merchandise.gender'),
        ),
    ]