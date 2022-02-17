from django.conf.urls import patterns, url

urlpatterns = patterns('', 
                       url('^$', 'echo.views.echo', name='echo'),
                       url(r'^ajax$', 'echo.views.ajaxtest', name="ajaxtest"),
                       )
