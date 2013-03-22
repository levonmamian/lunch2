from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'lunch2.views.home', name='home'),
    url(r'^lunch2/$', 'lunch2.views.home', name='home'),
    url(r'^lunch2/login/$', 'lunch2.views.login', name='login'),
    url(r'^lunch2/login_post/$', 'lunch2.views.login_post', name='login_post'),
    url(r'^lunch2/resetpassword/$', 'lunch2.views.resetpassword', name='resetpassword'),
    url(r'^lunch2/resetpassword_post/$', 'lunch2.views.resetpassword_post', name='resetpassword_post'),
    url(r'^lunch2/logout/$', 'lunch2.views.logout_view', name='logout_view'),
    url(r'^lunch2/register/$', 'lunch2.views.register', name='register'),
    url(r'^lunch2/register_post/$', 'lunch2.views.register_post', name='register_post'),
    url(r'^lunch2/restaurant/$', 'lunch2.views.allrestaurants', name='restaurant'),
    url(r'^lunch2/mealorder/$', 'lunch2.views.allmealorders', name='mealorder'),
	url(r'^lunch2/restaurant/(?P<restaurant_id>\d+)/$', 'lunch2.views.restaurantdetail', name='restaurantdetail'),
    url(r'^lunch2/mealorder/(?P<mealorder_id>\d+)/$', 'lunch2.views.mealorderdetail', name='mealorderdetail'),
    url(r'^lunch2/mealorder/(?P<mealorder_id>\d+)/enterorder/$', 'lunch2.views.enterorder', name='enterorder'),
    url(r'^lunch2/mealorder/(?P<mealorder_id>\d+)/summary/$', 'lunch2.views.pastmealorder', name='pastmealorder'),
    #url(r'^$', 'lunch2.views.home', name='home'),
    # url(r'^lunch2/', include('lunch2.foo.urls')),
	# url(r'^lunch2/', include('lunch2.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
