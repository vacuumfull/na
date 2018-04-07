from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20180407_2015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='Google',
            old_name='system_username',
            new_name='system_id'
        ),
    ]