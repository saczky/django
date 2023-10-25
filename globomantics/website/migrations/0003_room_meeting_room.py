# Generated by Django 4.2.5 on 2023-09-15 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_meeting_duration_meeting_start_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('floor', models.IntegerField()),
                ('room_number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='meeting',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='website.room'),
            preserve_default=False,
        ),
    ]