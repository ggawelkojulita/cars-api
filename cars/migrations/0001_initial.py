# Generated by Django 3.1.3 on 2021-02-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make_name', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('make_name', 'model_name')},
            },
        ),
    ]
