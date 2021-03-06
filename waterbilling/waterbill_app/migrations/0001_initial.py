# Generated by Django 3.2 on 2021-10-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumerlist',
            fields=[
                ('account_id', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('meter_number', models.CharField(blank=True, max_length=45, null=True)),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'consumerinfo',
            },
        ),
    ]
