# Generated by Django 2.2.4 on 2019-11-26 17:03

from django.db import migrations, models


def update_default_name(apps, schema_editor):
    Group = apps.get_model("management", "Group")
    for group in Group.objects.all():
        if group.system:
            group.name = "Default user access"
            group.save()


class Migration(migrations.Migration):

    dependencies = [("management", "0010_group_system")]

    operations = [migrations.RunPython(update_default_name)]
