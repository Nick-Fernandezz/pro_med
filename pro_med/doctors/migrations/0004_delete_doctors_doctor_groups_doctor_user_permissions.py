# Generated by Django 5.0.3 on 2024-03-21 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('doctors', '0003_doctor'),
        ('pacients', '0003_alter_therapeuticanddiagnosticevents_doctor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Doctors',
        ),
        migrations.AddField(
            model_name='doctor',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
