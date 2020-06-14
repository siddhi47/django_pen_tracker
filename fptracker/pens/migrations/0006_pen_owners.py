# Generated by Django 3.0.5 on 2020-04-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('pens', '0005_pen_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='pen',
            name='owners',
            field=models.ManyToManyField(related_name='pens', to='users.Profile'),
        ),
    ]
