# Generated by Django 3.1.1 on 2020-09-11 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='BinOperation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('collection_frequency', models.IntegerField()),
                ('last_collection', models.DateTimeField()),
                ('bin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigation.bin')),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('bin', models.ManyToManyField(through='navigation.BinOperation', to='navigation.Bin')),
            ],
        ),
        migrations.AddField(
            model_name='binoperation',
            name='operation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigation.operation'),
        ),
    ]