from django.conf.urls import patterns, url
#from django.contrib.auth import views as auth_views

urlpatterns = patterns("",
                        #url('login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, name='login'),
                        url('login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}, name='login'),
                        url('logout/$', 'django.contrib.auth.views.logout',{'next_page':'/'}, name='logout'),
                       )
