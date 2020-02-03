# Generated by Django 3.0.2 on 2020-02-01 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts', '0002_auto_20200130_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Posts.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]