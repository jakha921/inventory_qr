# Generated by Django 4.2.7 on 2024-07-16 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Korpus nomi')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Korpus manzili')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Korpus haqida malumot')),
            ],
            options={
                'verbose_name': 'Korpuslar',
                'verbose_name_plural': 'Korpus',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ismi')),
                ('surname', models.CharField(max_length=255, verbose_name='Familiyasi')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Otasining ismi')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefon raqami')),
                ('image', models.CharField(default='https://cdn4.iconfinder.com/data/icons/signicon-pt-1-1/100/041_-_user_profile_avatar_login_account-1024.png', max_length=255, verbose_name='Rasm')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('degree', models.CharField(blank=True, choices=[('O`rta', 'O`rta'), ('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr'), ('Doktorant', 'Doktorant'), ('Professor', 'Professor'), ('Akademik', 'Akademik')], default='O`rta', max_length=255, null=True, verbose_name='Ilmiy darajasi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Qisqacha ma`lumot')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/', verbose_name='Rasm')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Xodimlar',
                'verbose_name_plural': 'Xodimlar',
                'ordering': ['surname', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Inventar nomi')),
                ('number', models.CharField(blank=True, max_length=500, null=True, verbose_name='Inventar raqami')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Inventar haqida malumot')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='inventories/', verbose_name='Inventar rasmi')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Inventar narxi')),
                ('count', models.IntegerField(blank=True, null=True, verbose_name='Invenrar soni')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Inventarlar',
                'verbose_name_plural': 'Inventar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=255, verbose_name='Xona raqami')),
                ('corpus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.corpus', verbose_name='Korpus')),
                ('room_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.employee', verbose_name='Xona masul xodim')),
            ],
            options={
                'verbose_name': 'Xonalar',
                'verbose_name_plural': 'Xona',
                'ordering': ['room_number'],
            },
        ),
        migrations.CreateModel(
            name='RoomInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Soni')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.inventory', verbose_name='Inventar nomi')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room', verbose_name='Xona raqami')),
            ],
            options={
                'verbose_name': 'Xonadagi inventarlar',
                'verbose_name_plural': 'Xonadagi inventar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='EmployeeInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Soni')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee', verbose_name='Xodim')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.inventory', verbose_name='Inventar nomi')),
            ],
            options={
                'verbose_name': 'Xodimlardagi inventarlar',
                'verbose_name_plural': 'Xodimdagi inventar',
                'ordering': ['-created_at'],
            },
        ),
    ]
