# Generated by Django 5.1.1 on 2024-10-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_booknote_created_at_booknote_note_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbook',
            name='pages',
            field=models.IntegerField(default=0),
        ),
    ]
