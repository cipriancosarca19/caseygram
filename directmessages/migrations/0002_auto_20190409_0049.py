# Generated by Django 2.1.7 on 2019-04-09 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directmessages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-date_created']},
        ),
    ]
