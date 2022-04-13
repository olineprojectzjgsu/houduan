# Generated by Django 2.2.12 on 2022-04-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='', max_length=32)),
                ('email', models.EmailField(max_length=32)),
                ('pwd', models.CharField(default='', max_length=32)),
                ('phone', models.IntegerField(default=0)),
                ('nickname', models.CharField(default='', max_length=20)),
            ],
        ),
    ]
