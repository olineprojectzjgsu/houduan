# Generated by Django 2.2.12 on 2022-04-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='describation',
            field=models.TextField(default='', max_length=288, verbose_name='描述'),
        ),
        migrations.AddField(
            model_name='product',
            name='saler_id',
            field=models.IntegerField(default=1, verbose_name='商家ID'),
        ),
        migrations.AddField(
            model_name='product',
            name='sort',
            field=models.CharField(default='', max_length=50, verbose_name='产品分类'),
        ),
    ]
