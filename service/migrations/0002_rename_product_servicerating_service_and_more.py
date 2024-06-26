# Generated by Django 5.0.3 on 2024-04-06 08:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerating',
            old_name='product',
            new_name='service',
        ),
        migrations.RenameField(
            model_name='servicereview',
            old_name='product',
            new_name='service',
        ),
        migrations.AlterUniqueTogether(
            name='servicerating',
            unique_together={('service', 'user')},
        ),
    ]
