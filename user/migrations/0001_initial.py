# Generated by Django 2.2.7 on 2019-11-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField()),
                ('user_age', models.IntegerField()),
                ('user_phone', models.TextField()),
                ('user_address', models.TextField()),
            ],
        ),
    ]
