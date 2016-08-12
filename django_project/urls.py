from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
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
    url(r'^oops', views.oops, name='oops'),
    url(r'^about$', views.about, name='about'),
    url(r'^product$', views.product, name='product'),
    url(r'^solution$', views.solution, name='solution'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^contact-form$', views.contact_form, name='contact-form'),
    #url(r'^submit_email/$', views.submit_email, name='submit_email'),
    #url(r'^team/$', views.team, name='team'),
    #url(r'^press/$', views.press, name='press'),
    url(r'^thankyou', views.submit_email, name='thankyou'),
    url(r'^.*/$', RedirectView.as_view(url='/oops')),
)

urlpatterns += staticfiles_urlpatterns()