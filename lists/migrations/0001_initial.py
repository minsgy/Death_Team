# Generated by Django 3.1.1 on 2020-09-06 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0002_auto_20200906_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('now', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=20, null=True)),
                ('content', models.TextField(blank=True, default='')),
                ('photos', models.ImageField(upload_to='list_photos')),
                ('name', models.CharField(max_length=20, null=True)),
                ('groups', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='groups.group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
