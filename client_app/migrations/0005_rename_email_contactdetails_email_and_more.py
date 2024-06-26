# Generated by Django 5.0.1 on 2024-03-12 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0004_contactdetails'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactdetails',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contactdetails',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contactdetails',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contactdetails',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='clientdetails',
            name='price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
