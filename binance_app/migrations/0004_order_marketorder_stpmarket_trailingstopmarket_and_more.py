# Generated by Django 4.0.2 on 2022-02-15 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('binance_app', '0003_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=15)),
                ('side', models.CharField(choices=[('BUY', 'BUY'), ('SELL', 'SELL')], max_length=4)),
                ('type', models.CharField(choices=[('LIMIT', 'LIMIT'), ('MARKET', 'MARKET'), ('STOP', 'STOP'), ('TAKE_PROFIT', 'TAKE_PROFIT'), ('STOP_MARKET', 'STOP_MARKET'), ('TAKE_PROFIT_MARKET', 'TAKE_PROFIT_MARKET'), ('TRAILING_STOP_MARKET', 'TRAILING_STOP_MARKET')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='MarketOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='binance_app.order')),
                ('quantity', models.FloatField()),
            ],
            bases=('binance_app.order',),
        ),
        migrations.CreateModel(
            name='STPMarket',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='binance_app.order')),
                ('stopPrice', models.FloatField()),
            ],
            bases=('binance_app.order',),
        ),
        migrations.CreateModel(
            name='TrailingStopMarket',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='binance_app.order')),
                ('callbackRate', models.FloatField()),
            ],
            bases=('binance_app.order',),
        ),
        migrations.CreateModel(
            name='LimitOrder',
            fields=[
                ('marketorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='binance_app.marketorder')),
                ('timeInForce', models.CharField(choices=[('GTC', 'GTC'), ('IOC', 'IOC'), ('FOK', 'FOK'), ('GTX', 'GTX')], max_length=4)),
                ('price', models.FloatField()),
            ],
            bases=('binance_app.marketorder',),
        ),
        migrations.CreateModel(
            name='STPLimit',
            fields=[
                ('marketorder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='binance_app.marketorder')),
                ('stopPrice', models.FloatField()),
            ],
            bases=('binance_app.marketorder',),
        ),
    ]
