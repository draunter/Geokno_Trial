# Generated by Django 2.0.5 on 2018-05-25 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Input', '0002_auto_20180525_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dem',
            name='Lidar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Input.AirborneLidar'),
        ),
        migrations.AlterField(
            model_name='dem',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Input.Album'),
        ),
        migrations.AlterField(
            model_name='dem',
            name='son',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Input.Son'),
        ),
    ]
