from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from decouple import config


admin.autodiscover()
admin.site.site_header = config('SITE_HEADER')
admin.site.site_title = config('SITE_TITLE')


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + [

    re_path(r'(?P<path>.*)', TemplateView.as_view(
        template_name="index.html"),
        name='base-home')

]
