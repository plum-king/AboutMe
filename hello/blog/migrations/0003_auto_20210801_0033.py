# Generated by Django 3.2.3 on 2021-07-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(default='', upload_to='images/ ')),
                ('explain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(default='', upload_to='images/ ')),
                ('explain', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(default='', upload_to='images/ ')),
                ('explain', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Blog',
            new_name='Hobby',
        ),
    ]
