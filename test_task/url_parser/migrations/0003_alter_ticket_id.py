# Generated by Django 4.0.1 on 2022-01-11 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_parser', '0002_alter_ticket_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]