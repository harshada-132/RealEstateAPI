# Generated by Django 5.0 on 2024-02-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=255)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('negotiable', models.BooleanField()),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
    ]
