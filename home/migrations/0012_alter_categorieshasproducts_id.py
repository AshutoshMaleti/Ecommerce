# Generated by Django 3.2.7 on 2021-09-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210927_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorieshasproducts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
