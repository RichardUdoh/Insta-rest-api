# Generated by Django 3.1.4 on 2020-12-23 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201223_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.like'),
        ),
    ]
