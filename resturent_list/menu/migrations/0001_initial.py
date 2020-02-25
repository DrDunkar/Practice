# Generated by Django 2.2.5 on 2020-02-23 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='restro_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.CharField(max_length=30)),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
