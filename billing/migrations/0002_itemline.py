# Generated by Django 4.2.6 on 2023-10-17 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('texted', models.BooleanField()),
                ('Invoice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='billing.invoice')),
            ],
        ),
    ]
