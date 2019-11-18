# Generated by Django 2.2.2 on 2019-07-18 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config. ', max_length=31, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=31)),
                ('slug', models.SlugField(help_text='A label for URL config. ', max_length=31, unique=True)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='date founded')),
                ('contact', models.URLField()),
                ('website', models.URLField(max_length=255)),
                ('tags', models.ManyToManyField(to='organizer.Tag')),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'founded_date',
            },
        ),
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='Date published')),
                ('link', models.URLField(max_length=255)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='organizer.Startup')),
            ],
            options={
                'verbose_name': 'news article',
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
            },
        ),
    ]
