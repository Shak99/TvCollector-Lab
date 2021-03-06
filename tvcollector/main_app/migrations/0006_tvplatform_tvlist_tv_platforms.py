# Generated by Django 4.0.4 on 2022-04-28 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_show_studio_tv'),
    ]

    operations = [
        migrations.CreateModel(
            name='TvPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plat_name', models.CharField(max_length=250)),
                ('plat_type', models.CharField(choices=[('Web', 'Web Platform'), ('Cable', 'Cable Television')], default='Web', max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='tvlist',
            name='tv_platforms',
            field=models.ManyToManyField(to='main_app.tvplatform'),
        ),
    ]
