# Generated by Django 2.1.2 on 2018-11-01 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='negativeTweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetText', models.TextField(max_length=1000)),
                ('userName', models.TextField(default='no username', max_length=200)),
                ('time', models.TextField(default='no time', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='positiveTweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetText', models.TextField(max_length=1000)),
                ('userName', models.TextField(default='no username', max_length=200)),
                ('time', models.TextField(default='no time', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tweetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.TextField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
