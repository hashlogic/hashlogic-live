# Generated by Django 3.2.6 on 2021-09-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comments_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='post_pics'),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default='', max_length=1000),
        ),
    ]