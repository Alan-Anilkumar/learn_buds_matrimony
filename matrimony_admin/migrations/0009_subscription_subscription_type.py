# Generated by Django 5.0.8 on 2024-09-28 07:19

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('matrimony_admin', '0008_alter_subscriptioninfo_sub'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subscription_type',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
