from django.conf.urls import patterns, url

urlpatterns = patterns('lunch2.views',
    url(r'^$', 'home'),
    #url(r'^(?P<restaurant_id>\d+)/$', 'restaurantdetail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)

urlpatterns = patterns('lunch2.views',
    url(r'^$', 'allrestaurants'),
    #url(r'^(?P<restaurant_id>\d+)/$', 'restaurantdetail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)

urlpatterns = patterns('lunch2.views.mealorder',
    url(r'^$', 'home'),
    #url(r'^(?P<restaurant_id>\d+)/$', 'restaurantdetail'),
    #url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    #url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)