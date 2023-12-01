# Generated by Django 4.2.7 on 2023-11-06 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_additionalexpense_inventory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Xodimlar', 'verbose_name_plural': 'Xodimlar'},
        ),
        migrations.AlterModelOptions(
            name='teacherinventory',
            options={'verbose_name': 'Xodimlardagi inventarlar', 'verbose_name_plural': 'Xodimdagi inventar'},
        ),
        migrations.AlterField(
            model_name='roominventory',
            name='inventory',
            field=models.ForeignKey(limit_choices_to={'warehouse__status': 'Omborda'}, on_delete=django.db.models.deletion.CASCADE, to='app.inventory', verbose_name='Inventar nomi'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.room', verbose_name='Ma`sul xona'),
        ),
        migrations.AlterField(
            model_name='teacherinventory',
            name='inventory',
            field=models.ForeignKey(limit_choices_to={'warehouse__status': 'Omborda'}, on_delete=django.db.models.deletion.CASCADE, to='app.inventory', verbose_name='Inventar nomi'),
        ),
    ]
