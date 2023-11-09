# Generated by Django 4.2.6 on 2023-10-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payables',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'paid'), ('W', 'waiting_founds')], max_length=1)),
                ('payment_date', models.DateField()),
                ('avaliable_founds', models.FloatField()),
                ('waiting_founds', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_value', models.FloatField()),
                ('description_transaction', models.CharField(max_length=100)),
                ('payment_method', models.CharField(choices=[('D', 'debit_card'), ('C', 'credit_card')], max_length=1)),
                ('card_number', models.IntegerField()),
                ('customer_name', models.CharField(max_length=50)),
                ('expiration_date', models.DateField()),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
