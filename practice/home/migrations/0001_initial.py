# Generated by Django 2.2.5 on 2020-02-09 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='resturent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='image/')),
                ('Name', models.CharField(max_length=30)),
                ('Addresses', models.CharField(max_length=30)),
                ('vat_no', models.IntegerField()),
            ],
        ),
    ]
