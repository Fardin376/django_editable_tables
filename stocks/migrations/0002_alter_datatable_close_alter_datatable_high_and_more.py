# Generated by Django 4.1 on 2023-09-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatable',
            name='close',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='high',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='low',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='datatable',
            name='open',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
