from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf.urls.static import static
# from django.contrib import admin
#
# admin.autodiscover()
from WorkStudio import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'WorkStudio.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', TemplateView.as_view(template_name="main.html")),
                       url(r'^dev/$', TemplateView.as_view(template_name="dev.html")),
                       url(r'^orign/$', TemplateView.as_view(template_name="orign.html")),
                       # url(r'^$', TemplateView.as_view(template_name="main.html")),
                       # url(r'^/', include(admin.site.urls)),
)
