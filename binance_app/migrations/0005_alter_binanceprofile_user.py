# Generated by Django 4.0.2 on 2022-02-16 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_bio_insight_followerscount'),
        ('binance_app', '0004_order_marketorder_stpmarket_trailingstopmarket_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binanceprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]