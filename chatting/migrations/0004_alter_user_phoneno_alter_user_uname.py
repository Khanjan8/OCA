# Generated by Django 5.0.2 on 2024-03-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0003_alter_user_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneno',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(default='Default', max_length=30),
        ),
    ]
