# Generated by Django 3.0.8 on 2020-07-18 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(unique='True')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DataOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
                ('data_tracker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.DataTracker')),
            ],
            options={
                'unique_together': {('name', 'data_tracker')},
            },
        ),
        migrations.CreateModel(
            name='DataResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.DataOption')),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Entry')),
            ],
            options={
                'unique_together': {('entry', 'data_option')},
            },
        ),
    ]
