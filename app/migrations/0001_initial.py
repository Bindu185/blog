# Generated by Django 4.1.1 on 2022-09-12 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=50)),
                ('booktitle', models.CharField(max_length=50)),
                ('studentid', models.IntegerField()),
                ('publicationid', models.IntegerField()),
                ('authorname', models.TextField()),
            ],
        ),
    ]
