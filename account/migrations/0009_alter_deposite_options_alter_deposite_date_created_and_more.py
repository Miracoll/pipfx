# Generated by Django 4.1.7 on 2024-03-11 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_deposite_amount_alter_deposite_date_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposite',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='deposite',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 11, 20, 17, 6, 263495), null=True),
        ),
        migrations.AlterField(
            model_name='deposite',
            name='expire_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 11, 21, 17, 6, 263495), null=True),
        ),
    ]
