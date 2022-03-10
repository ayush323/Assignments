# Generated by Django 4.0.3 on 2022-03-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_tag_post_post_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(related_name='tag', to='blog.post'),
        ),
    ]
