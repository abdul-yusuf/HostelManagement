# Generated by Django 4.1.6 on 2023-02-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_is_admin_user_phone_no_user_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]