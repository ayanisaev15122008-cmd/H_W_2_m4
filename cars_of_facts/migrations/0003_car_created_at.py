from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_of_facts', '0002_alter_car_options_remove_car_facts'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
