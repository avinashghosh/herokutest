# Generated by Django 3.0.3 on 2020-03-05 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_college_college_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='college_catagory',
            new_name='collegecatagory',
        ),
    ]
