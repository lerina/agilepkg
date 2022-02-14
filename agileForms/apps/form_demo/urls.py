from django.conf.urls import patterns, url

urlpatterns = patterns('', 
                       url('^$', 'form_demo.views.formDemoIndex', name="formDemoIndex"),
                       url('^simpleForm/$', 'form_demo.views.showSimpleFormDemoForm', name="simpleForm"),
                       url('^tmplTags/$', 'form_demo.views.showSimpleFormDemoBootstrapUsingTemplateTagsForm', name="tmplTagsForm"),
                       url('^crispyModelForm/$', 'form_demo.views.showSimpleFormDemoBootstrapUsingCrispyModelForm', name="crispyModelForm"),
                       url('^modalFormSkinned/$', 'form_demo.views.modalFormSkinned', name="modalFormSkinned"),
                       url('^modalForm/$', 'form_demo.views.showModalFormDemoForm', name="modalForm"),
                       )
