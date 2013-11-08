from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
# from django.contrib import admin
#
# admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'WorkStudio.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', TemplateView.as_view(template_name="main.html")),
                       # url(r'^/', include(admin.site.urls)),
)
