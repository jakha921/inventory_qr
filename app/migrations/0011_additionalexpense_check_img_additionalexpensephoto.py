# Generated by Django 4.2.7 on 2023-11-30 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_teacher_options_alter_teacherinventory_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalexpense',
            name='check_img',
            field=models.ImageField(blank=True, null=True, upload_to='checks/', verbose_name='Chek rasmi'),
        ),
        migrations.CreateModel(
            name='AdditionalExpensePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='additional_expense_photos/', verbose_name='Rasm')),
                ('additional_expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.additionalexpense', verbose_name='Xarajat')),
            ],
            options={
                'verbose_name': 'Xarajat rasmlari',
                'verbose_name_plural': 'Xarajatlar rasmlari',
            },
        ),
    ]
