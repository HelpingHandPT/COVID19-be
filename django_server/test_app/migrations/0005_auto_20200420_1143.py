# Generated by Django 3.0.4 on 2020-04-20 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0004_auto_20200420_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthlog',
            name='patient_id',
            field=models.OneToOneField(db_column='userId', limit_choices_to=models.Q(('user_type', 201), ('user_type', 200), _connector='OR'), on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
