# Generated by Django 3.2.6 on 2021-09-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0003_rooms_rndid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='rooms',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]