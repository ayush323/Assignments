# Generated by Django 4.0.3 on 2022-03-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_first_name_author_firstname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(related_name='oost', to='blog.tag'),
        ),
    ]
