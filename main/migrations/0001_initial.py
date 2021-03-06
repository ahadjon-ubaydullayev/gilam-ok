# Generated by Django 3.2.9 on 2022-07-03 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(blank=True, max_length=256, null=True)),
                ('size', models.CharField(blank=True, max_length=128, null=True)),
                ('price', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=256)),
                ('active', models.BooleanField(default=True)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=256)),
                ('active', models.BooleanField(default=True)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('status', models.CharField(max_length=256)),
                ('active', models.BooleanField(default=True)),
                ('cr_on', models.DateTimeField(auto_now_add=True)),
                ('cr_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
