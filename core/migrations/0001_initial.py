# Generated by Django 3.0.8 on 2020-07-31 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connector', models.IntegerField(verbose_name='Connector Port')),
                ('shutdown', models.IntegerField(verbose_name='Shutdown Port')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=3, verbose_name='Initials')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('link', models.CharField(max_length=100, verbose_name='Link')),
                ('version', models.DateField(verbose_name='Version')),
                ('status', models.CharField(choices=[('1', 'OK'), ('2', 'Suspenso'), ('3', 'Com Problema')], default='1', max_length=1, verbose_name='Status')),
                ('port', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Port')),
                ('system', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.System')),
            ],
        ),
    ]
