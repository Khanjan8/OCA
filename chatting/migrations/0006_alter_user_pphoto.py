# Generated by Django 5.0.2 on 2024-03-29 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0005_alter_user_phoneno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pphoto',
            field=models.ImageField(upload_to=''),
        ),
    ]