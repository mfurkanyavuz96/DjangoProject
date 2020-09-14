# Generated by Django 3.1.1 on 2020-09-10 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plate', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='NavigationRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navigation.vehicle')),
            ],
        ),
    ]
