# Generated by Django 4.0.2 on 2023-03-20 11:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=64)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('licenses', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=16)),
                ('status', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.school')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.school'),
        ),
        migrations.AddIndex(
            model_name='license',
            index=models.Index(fields=['token'], name='api_license_token_5d302d_idx'),
        ),
    ]
