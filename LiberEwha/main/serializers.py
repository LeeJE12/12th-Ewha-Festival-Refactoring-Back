from rest_framework import serializers
from booths.models import Booth, Menu
from notice.models import Notice
from booths.serializers import *
from shows.serializers import *
from notice.serializers import *
from django.utils.dateformat import format


class ScrapSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    type = serializers.CharField()  # 부스, 공연, 메뉴 타입 구분


class MainPageBoothSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    class Meta:
        model = Booth
        fields = ['id', 'name', 'thumbnail', 'category',
                  'booth_place', 'is_opened', 'scrap_count', 'type']

    def get_type(self, obj):
        return 'show' if obj.is_show else 'booth'

class MainPageMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'booth', 'menu', 'price',
                  'img', 'is_vegan', 'is_soldout', 'scrap_count']

class SearchResultSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.SerializerMethodField()
    booth_place = serializers.SerializerMethodField()
    menu = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField(allow_null=True)
    is_opened = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    scrap_count = serializers.SerializerMethodField()


    def get_name(self, obj):
        if isinstance(obj, Booth):
            return obj.name
        elif isinstance(obj, Menu):
            return obj.booth.name  # 메뉴의 부스 이름을 표시
        elif isinstance(obj, Notice):
            return obj.title
        return None

    def get_booth_place(self, obj):
        if isinstance(obj, Booth):
            return obj.place
        return None

    def get_scrap_count(self, obj):
        if isinstance(obj, Booth):
            return obj.scrap_count
        elif isinstance(obj, Menu):
            return obj.scrap_count
        return None

    def get_menu(self, obj):
        if isinstance(obj, Menu):
            return obj.menu  # Menu 객체에서의 메뉴 이름
        return None  # Booth나 Notice에서는 해당되지 않음

    def get_category(self, obj):
        if isinstance(obj, Booth):
            return obj.category
        elif isinstance(obj, Menu):
            return obj.booth.category  # 메뉴는 속한 부스의 카테고리를 사용할 수 있음
        return None  # Notice는 카테고리가 없음

    def get_description(self, obj):
        if isinstance(obj, Booth):
            return obj.description
        elif isinstance(obj, Menu):
            return f"{obj.menu} - {obj.price}원"  # 메뉴의 설명을 간단히 작성
        elif isinstance(obj, Notice):
            return obj.content
        return None

    def get_type(self, obj):
        if isinstance(obj, Booth):
            return 'show' if obj.is_show else 'booth'
        elif isinstance(obj, Menu):
            return 'menu'
        elif isinstance(obj, Notice):
            return 'notice'
        return 'unknown'

    def get_thumbnail(self, obj):
        if isinstance(obj, Booth):
            if obj.thumbnail and obj.thumbnail.name:
                return obj.thumbnail.url
        return None

    def get_is_opened(self, obj):
        if isinstance(obj, Booth):
            return obj.is_opened
        return False

    def get_author(self, obj):
        if isinstance(obj, Notice):
            return {'id': obj.author.id, 'nickname': obj.author.nickname }
        return False

    def get_created_at(self, obj):
        if isinstance(obj, Notice):
            return format(obj.created_at, 'Y-m-d')
        return False