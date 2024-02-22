# Generated by Django 4.1 on 2024-01-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'مراجع', 'verbose_name_plural': 'مراجعین'},
        ),
        migrations.AlterModelOptions(
            name='reasontovisit',
            options={'verbose_name': 'دلیل مراجعه', 'verbose_name_plural': 'دلایل مراجعه'},
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=250, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=250, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=100, verbose_name='تلفن همراه'),
        ),
        migrations.AlterField(
            model_name='person',
            name='reasons_to_visit',
            field=models.ManyToManyField(related_name='people', to='crm.reasontovisit', verbose_name='دلایل مراجعه'),
        ),
    ]