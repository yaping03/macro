# Generated by Django 2.0.1 on 2019-05-10 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ns1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ns1_3d_detail',
            name='id',
        ),
        migrations.AlterField(
            model_name='ns1_3d_detail',
            name='PDB_ID',
            field=models.CharField(max_length=32, primary_key=True, serialize=False),
        ),
    ]