from django.urls import path
from django.conf import settings
from booths.views import *

app_name = 'booths'

urlpatterns=[
    path('main/', BoothsMainView.as_view()),
    path('<int:pk>/', BoothsDetailView.as_view()),
    path('<int:pk>/scrap/', BoothScrapView.as_view()),
    path('<int:pk>/menus/<int:menu_id>/scrap/', MenuScrapView.as_view())

]