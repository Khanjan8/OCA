# Generated by Django 5.0.2 on 2024-03-31 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('uid', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('uname', models.CharField(default='Default', max_length=30)),
                ('about', models.CharField(default='Available', max_length=30)),
                ('pphoto', models.ImageField(default='defaultprofile.jpg', upload_to='')),
                ('phoneno', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_sender', to='chatting.user')),
                ('uid2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='req_reciever', to='chatting.user')),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportmsg', models.TextField()),
                ('uid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report_sender', to='chatting.user')),
                ('uid2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reprot_reciver', to='chatting.user')),
            ],
        ),
        migrations.CreateModel(
            name='pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pin_sender', to='chatting.user')),
                ('uid2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pin_reciver', to='chatting.user')),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('uid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to='chatting.user')),
                ('uid2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_reciever', to='chatting.user')),
            ],
        ),
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.BinaryField()),
                ('uid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_sender', to='chatting.user')),
                ('uid2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_reciever', to='chatting.user')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedbackmsg', models.TextField()),
                ('uid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='chatting.user')),
            ],
        ),
        migrations.CreateModel(
            name='block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_sender', to='chatting.user')),
                ('uid2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='block_reciver', to='chatting.user')),
            ],
        ),
        migrations.CreateModel(
            name='admin2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='chatting.user')),
            ],
        ),
    ]
