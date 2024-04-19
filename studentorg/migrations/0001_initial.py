# Generated by Django 5.0.4 on 2024-04-19 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('college_name', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=250)),
                ('descriptoin', models.CharField(max_length=500)),
                ('college', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='studentorg.college')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('prog_name', models.CharField(max_length=150)),
                ('College', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentorg.college')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=25)),
                ('firstname', models.CharField(max_length=25)),
                ('middlename', models.CharField(blank=True, max_length=25, null=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentorg.program')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrgMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('date_joined', models.DateField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentorg.organization')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentorg.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
