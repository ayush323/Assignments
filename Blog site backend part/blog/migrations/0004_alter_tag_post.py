# Generated by Django 4.0.3 on 2022-03-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, related_name='Tag', to='blog.post'),
        ),
    ]
