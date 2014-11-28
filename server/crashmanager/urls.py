from django.conf.urls import patterns, include, url
from rest_framework import routers
from crashmanager import views
from server import settings
import os

router = routers.DefaultRouter()
router.register(r'signatures', views.BucketViewSet)
router.register(r'crashes', views.CrashEntryViewSet)

urlpatterns = patterns('',
    url(r'^rest/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^signatures/$', views.signatures, name='signatures'),
    url(r'^signatures/all/$', views.allSignatures, name='allsignatures'),
    url(r'^signatures/new/$', views.newSignature, name='signew'),
    url(r'^signatures/(?P<sigid>\d+)/edit/$', views.editSignature, name='sigedit'),
    url(r'^signatures/(?P<sigid>\d+)/link/$', views.linkSignature, name='siglink'),
    url(r'^signatures/(?P<sigid>\d+)/$', views.viewSignature, name='sigview'),
    url(r'^signatures/(?P<sigid>\d+)/delete/$', views.deleteSignature, name='sigdel'),
    url(r'^crashes/$', views.crashes, name='crashes'),
    url(r'^crashes/all/$', views.allCrashes, name='allcrashes'),
    url(r'^crashes/autoassign/$', views.autoAssignCrashEntries, name='autoassign'),
    url(r'^crashes/(?P<crashid>\d+)/$', views.viewCrashEntry, name='crashview'),
    url(r'^crashes/(?P<crashid>\d+)/edit/$', views.editCrashEntry, name='crashedit'),
    url(r'^crashes/(?P<crashid>\d+)/delete/$', views.deleteCrashEntry, name='crashdel'),
    url(r'^crashes/(?P<crashid>\d+)/createbug/$', views.createExternalBug, name='createbug'),
    url(r'^bugprovider/(?P<providerId>\d+)/templates/create/$', views.createBugTemplate, name='createtemplate'),
    url(r'^bugprovider/(?P<providerId>\d+)/templates/(?P<templateId>\d+)/$', views.viewEditBugTemplate, name='viewtemplate'),

    
    url(r'^rest/', include(router.urls)),
)

# This makes Django serve our testcases from the tests/ URL. When hosting this
# project in production, one should consider serving tests directly through
# the webserver rather than through Django for performance reasons.
urlpatterns += patterns('', url(r'^tests/(.*)$', 'django.views.static.serve', name='download', kwargs={'document_root': os.path.join(settings.BASE_DIR, 'tests')}), )
