# Generated by Django 3.1.7 on 2021-03-06 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='Product', to='ProductApp.Category'),
        ),
    ]