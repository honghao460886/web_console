from django.conf.urls import patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from angel.views import login, home, logout

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'angel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^$', home),
    (r'^user/login/$', login),
    (r'^user/logout/$', logout)
)
urlpatterns += staticfiles_urlpatterns()