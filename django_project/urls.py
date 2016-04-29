from django.conf.urls import patterns, include, url

from django.contrib import admin
from placeholder import views
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin103759/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^product$', views.product, name='product'),
    url(r'^solution$', views.solution, name='solution'),
    url(r'^contact-form$', views.contact_form, name='contact-form'),
    #url(r'^submit_email/$', views.submit_email, name='submit_email'),
    #url(r'^team/$', views.team, name='team'),
    #url(r'^press/$', views.press, name='press'),
    #url(r'^thankyou/$', views.thankyou, name='thankyou'),
)

urlpatterns += staticfiles_urlpatterns()