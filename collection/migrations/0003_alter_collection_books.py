# Generated by Django 5.1.1 on 2024-11-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_userbook_pages'),
        ('collection', '0002_alter_collection_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='books',
            field=models.ManyToManyField(related_name='collections', to='book.userbook'),
        ),
    ]