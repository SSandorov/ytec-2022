# Generated by Django 4.1.3 on 2022-11-09 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=200)),
                ('players', models.ManyToManyField(to='soccer.player')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points_1', models.IntegerField(default=0)),
                ('points_2', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('teams', models.ManyToManyField(to='soccer.team')),
            ],
        ),
    ]
