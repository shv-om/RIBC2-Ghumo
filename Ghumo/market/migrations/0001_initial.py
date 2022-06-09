# Generated by Django 4.0.4 on 2022-06-09 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=50)),
                ('district_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.IntegerField()),
                ('item_description', models.CharField(max_length=500)),
                ('item_photo', models.ImageField(upload_to='all_items')),
                ('district_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.district')),
                ('seller_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.seller')),
            ],
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_start_date', models.DateField()),
                ('event_end_date', models.DateField()),
                ('event_poster', models.ImageField(upload_to='event_posters')),
                ('artist_instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.artist')),
            ],
            options={
                'ordering': ['event_start_date'],
            },
        ),
    ]
