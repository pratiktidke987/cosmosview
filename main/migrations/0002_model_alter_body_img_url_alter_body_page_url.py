# Generated by Django 4.0.5 on 2022-06-19 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model_url', models.CharField(default='', max_length=500)),
                ('caption', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='body',
            name='img_url',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='body',
            name='page_url',
            field=models.CharField(default='', max_length=500),
        ),
    ]
