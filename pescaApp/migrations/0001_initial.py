# Generated by Django 4.1.2 on 2022-10-30 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'Cuenca',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Metodo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'Metodo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pesca',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('fecha', models.TextField(db_column='fecha')),
                ('peso', models.TextField(db_column='peso')),
            ],
            options={
                'db_table': 'Pesca',
                'managed': False,
            },
        ),
    ]
