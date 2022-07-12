# Generated by Django 4.0.6 on 2022-07-12 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_app', '0006_tag_order_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tag',
        ),
        migrations.AddField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(to='customers_app.tag'),
        ),
    ]
