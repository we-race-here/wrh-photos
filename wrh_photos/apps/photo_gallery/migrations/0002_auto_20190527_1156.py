# Generated by Django 2.2.1 on 2019-05-27 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='low_resolution',
            new_name='low_res_file',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='original',
            new_name='original_file',
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='thumbnail',
            new_name='preview_file',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='is_public',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='photo_location',
        ),
        migrations.AddField(
            model_name='photo',
            name='logo_position',
            field=models.CharField(choices=[('tl', 'Top-Left'), ('tc', 'Top-Center'), ('tr', 'Top-Right'), ('cl', 'Center-Left'), ('cc', 'Center-Center'), ('cr', 'Center-Right'), ('bl', 'Bottom-Left'), ('bc', 'Bottom-Center'), ('br', 'Bottom-Right')], default='br', max_length=2),
        ),
        migrations.AddField(
            model_name='photo',
            name='seen',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('location', models.CharField(max_length=128)),
                ('map_latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=9, null=True)),
                ('map_longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=10, null=True)),
                ('sponsor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photo_gallery.Sponsor')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='photo', to='photo_gallery.Event'),
        ),
    ]
