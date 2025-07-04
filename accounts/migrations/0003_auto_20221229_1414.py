# Generated by Django 3.2.16 on 2022-12-29 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221229_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, help_text='Enter Your Address Details', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, help_text='Enter Your City', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='house_no',
            field=models.CharField(blank=True, help_text='Enter House / Flat Number / Colony / Ward No. ', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skill',
            field=models.CharField(blank=True, help_text='About Your Skills - Things you do greatly', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, help_text='Enter Your State', max_length=200, null=True),
        ),
    ]
