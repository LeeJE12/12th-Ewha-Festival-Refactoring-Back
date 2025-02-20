from django.urls import path
from django.conf import settings
from shows.views import *
from booths.views import BoothScrapView
from booths.views import *
from booths.serializers import *

app_name = 'shows'

urlpatterns=[
    path('main/', ShowsMainView.as_view()),
    path('<int:pk>/', ShowsDetailView.as_view()),
    path('<int:pk>/scrap/', BoothScrapView.as_view()),
    path('<int:pk>/guestbook/', GuestBookUserView.as_view()),
    path('<int:pk>/guestbook/<int:guestbook_id>/', GuestBookDeleteView.as_view()),
]