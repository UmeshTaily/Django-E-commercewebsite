# Generated by Django 4.0.2 on 2022-02-19 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products_cetegory_products_image_products_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='desc',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
