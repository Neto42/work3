from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/works/', permanent=True)),
]
