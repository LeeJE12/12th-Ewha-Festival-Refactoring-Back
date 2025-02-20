from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from booths.models import *
from booths.serializers import *

class ManageMenuSerializer(serializers.ModelSerializer):
    booth_id = serializers.IntegerField(source='booth.id', read_only=True)  # booth_id 추가

    class Meta:
        model = Menu
        fields = ['id','booth_id','menu',
                'img', 'price',
                'is_vegan', 'is_soldout']

class ManageBoothSerializer(serializers.ModelSerializer):
    #booth_id = serializers.IntegerField(source='booth.id', read_only=True)
    menus = MenuMainSerializer(many=True, read_only=True)
    booth_place = serializers.SerializerMethodField()
    days = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField(allow_null=True)
    class Meta:
        model = Booth
        fields = ['id', 'name', 'booth_place', 'category',
                  'thumbnail', 'admin_contact', 'is_opened',
                  'description', 'is_show',
                  'menus', 'days']

    def get_booth_place(self, obj):
        return obj.booth_place()

    def get_thumbnail(self, obj):
        if obj.thumbnail and obj.thumbnail.name:
            return obj.thumbnail.url

    def get_days(self, obj):
        days = [f"{day.day}일 {day.dayofweek}요일 {day.opening_time} ~ {day.closing_time}"
                 for day in obj.days.all()]
        return days

class ManageSerializer(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField(allow_null=True)

    class Meta:
        model = Booth
<<<<<<< Updated upstream
        fields = ['id', 'name', 'category', 
                  'thumbnail', 'is_opened', 
                  'place', 'days']
=======
        fields = ['id', 'name', 'category',
                  'booth_category',
                  'thumbnail', 'is_opened',
                  'place', 'days']

>>>>>>> Stashed changes
    def get_days(self, obj):
        days = [f"{day.opening_time} ~ {day.closing_time}"
                 for day in obj.days.all()]
        return days

    def get_thumbnail(self, obj):
        if obj.thumbnail and obj.thumbnail.name:
            return obj.thumbnail.url

class BoothNoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booth_notice
        fields = ['notice_type', 'content', 'booth', 'created_at']

class BoothNoticeCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = ['notice_count']