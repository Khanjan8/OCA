# Generated by Django 5.0.2 on 2024-03-31 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0002_rename_uid_admin2_uid1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin2',
            name='uid1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='chatting.user'),
        ),
    ]