from django.contrib import admin
from django.urls import path

from share.views import HomeView, DisplayView, MyView, SearchView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('s/<code>', DisplayView.as_view(), name='display'),
    path('my/', MyView.as_view(), name='my'),
    path('search/', SearchView.as_view(), name='search'),
]