# Generated by Django 5.0 on 2025-02-22 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akcel', '0006_campaign_days_left_campaign_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
