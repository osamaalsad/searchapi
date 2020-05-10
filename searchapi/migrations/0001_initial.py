# Generated by Django 3.0.5 on 2020-05-09 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CommentAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=200)),
                ('comment', models.TextField(max_length=400)),
                ('status', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='UnknownSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=256)),
                ('num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SearchingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128)),
                ('URL', models.CharField(max_length=400)),
                ('Description', models.TextField()),
                ('ID', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='searchapi.Category', verbose_name='Category')),
            ],
        ),
    ]