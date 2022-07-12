# Generated by Django 4.0.6 on 2022-07-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_app', '0005_order_customer_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='customers_app.tag'),
        ),
    ]