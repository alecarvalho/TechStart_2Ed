# Generated by Django 3.1.7 on 2021-03-06 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductApp', '0003_auto_20210305_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='Product', to='ProductApp.Category'),
        ),
    ]
