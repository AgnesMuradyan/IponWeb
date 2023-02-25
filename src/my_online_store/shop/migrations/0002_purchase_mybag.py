# Generated by Django 4.1.6 on 2023-02-23 17:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_time', models.DateField(default=datetime.date.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
                ('items', models.ManyToManyField(to='shop.item')),
            ],
        ),
        migrations.CreateModel(
            name='MyBag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.customer')),
                ('items', models.ManyToManyField(to='shop.item')),
            ],
        ),
    ]