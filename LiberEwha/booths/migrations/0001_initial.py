# Generated by Django 5.0.3 on 2024-09-30 14:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('thumbnail', models.ImageField(upload_to='thumbnail')),
                ('place', models.CharField(choices=[('교육관', '교육관'), ('학문관', '학문관'), ('생활관', '생활관'), ('대강당', '대강당'), ('휴웃길', '휴웃길'), ('포스코관', '포스코관'), ('신세계관', '신세계관'), ('잔디광장', '잔디광장'), ('학관', '학관'), ('학문관광장', '학문관광장'), ('스포츠트랙', '스포츠트랙')], max_length=20)),
                ('category', models.CharField(choices=[('음식', '음식'), ('굿즈', '굿즈'), ('체험', '체험'), ('밴드', '밴드'), ('댄스', '댄스')], max_length=10, null=True)),
                ('admin_contact', models.CharField(max_length=50, unique=True)),
                ('is_opened', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('is_show', models.BooleanField(default=False)),
                ('scrap_count', models.IntegerField(default=0)),
                ('notice_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booths', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booth_notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_type', models.CharField(choices=[('판매공지', '판매공지'), ('운영공지', '운영공지')], max_length=10)),
                ('content', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice', to='booths.booth')),
            ],
        ),
        migrations.CreateModel(
            name='Booth_scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booth_scrap', to='booths.booth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booth_scrap', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('10', '10'), ('11', '11'), ('12', '12')], max_length=5)),
                ('dayofweek', models.CharField(choices=[('수', '수'), ('목', '목'), ('금', '금')], max_length=5)),
                ('opening_time', models.CharField(max_length=5)),
                ('closing_time', models.CharField(max_length=5)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='booths.booth')),
            ],
        ),
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guestbook', to='booths.booth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guestbook', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=14)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='menu_img')),
                ('is_vegan', models.CharField(choices=[('페스코', '페스코'), ('비건', '비건'), ('논비건', '논비건'), ('해당없음', '해당없음')], default='None', max_length=10)),
                ('is_soldout', models.BooleanField(default=False)),
                ('scrap_count', models.IntegerField(default=0)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menus', to='booths.booth')),
            ],
        ),
        migrations.CreateModel(
            name='Menu_scrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_scrap', to='booths.menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_scrap', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('guestbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='booths.guestbook')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
