# Generated by Django 5.1.1 on 2024-10-05 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booths', '0005_alter_booth_booth_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth',
            name='booth_category',
            field=models.CharField(blank=True, choices=[('메인행사', '메인행사'), ('기획부스', '기획부스'), ('권리팀부스', '권리팀부스'), ('대외협력팀부스', '대외협력팀부스')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='booth',
            name='category',
            field=models.CharField(choices=[('음식', '음식'), ('굿즈', '굿즈'), ('체험', '체험'), ('밴드', '밴드'), ('댄스', '댄스')], max_length=10, null=True),
        ),
    ]
