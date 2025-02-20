# Generated by Django 5.0.3 on 2024-09-30 14:56

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
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('content', models.TextField(max_length=800)),
                ('notice_type', models.CharField(choices=[('operational', '운영공지'), ('event', '행사공지')], max_length=20)),
                ('event_type', models.CharField(blank=True, choices=[('ewhagreenFe', '다시 돌아온 네가 그린 그린은 이화그린'), ('artistShow', '아티스트 공연'), ('movie_fe', '야간 영화제'), ('nightMarket', '야시장'), ('tugOfWar', '영산 줄다리기'), ('riceFe', '이화인 한솥밥 배부')], max_length=20, null=True)),
                ('is_important', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
