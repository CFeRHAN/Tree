# Generated by Django 4.0.2 on 2022-02-16 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio_insight_followerscount'),
        ('binance_app', '0007_rename_user_binanceprofile_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binanceprofile',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
