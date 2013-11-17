from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

# from django.contrib import admin
#
# admin.autodiscover()


#statics
urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'WorkStudio.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', TemplateView.as_view(template_name="main.html")),
                       url(r'^dev/$', TemplateView.as_view(template_name="dev.html")),
                       url(r'^orign/$', TemplateView.as_view(template_name="orign.html")),
                       url(r'^blog/$', TemplateView.as_view(template_name="blog.html")),
                       url(r'^tools/$', TemplateView.as_view(template_name="tools.html")),
                       url(r'^net/$', TemplateView.as_view(template_name="net.html")),

                       #demos
                       url(r'^demo/atx/$', TemplateView.as_view(template_name="demo/activex.html")),
                       url(r'^demo/bs/$', TemplateView.as_view(template_name="demo/bs.html")),
                       url(r'^demo/email/$', TemplateView.as_view(template_name="demo/email.html")),
                       url(r'^demo/ftp/$', TemplateView.as_view(template_name="demo/ftp.html")),
                       url(r'^demo/net/$', TemplateView.as_view(template_name="demo/net.html")),
                       url(r'^demo/wingui/$', TemplateView.as_view(template_name="demo/wingui.html")),

                       # url(r'^$', TemplateView.as_view(template_name="main.html")),
                       # url(r'^/', include(admin.site.urls)),

)
urlpatterns += staticfiles_urlpatterns()
