# Generated by Django 5.0.2 on 2024-03-29 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0004_alter_user_phoneno_alter_user_uname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phoneno',
            field=models.CharField(max_length=13),
        ),
    ]