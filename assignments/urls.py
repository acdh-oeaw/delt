from django.conf.urls import url
from . import views

app_name = 'assignments'

urlpatterns = [
    url(r'^assignments/$', views.AssignmentListView.as_view(), name='browse_assignments'),
    url(r'^assignment/detail/(?P<pk>[0-9]+)$', views.AssignmentDetailView.as_view(),
        name='assignment_detail'),
    url(r'^assignment/delete/(?P<pk>[0-9]+)$', views.AssignmentDelete.as_view(),
        name='assignment_delete'),
    url(r'^assignment/edit/(?P<pk>[0-9]+)$', views.AssignmentUpdate.as_view(),
        name='assignment_edit'),
    url(r'^assignment/create/$', views.AssignmentCreate.as_view(),
        name='assignment_create'),
    url(r'^texts/$', views.TextListView.as_view(), name='browse_texts'),
    url(r'^text/detail/(?P<pk>[0-9]+)$', views.TextDetailView.as_view(),
        name='text_detail'),
    url(r'^text/delete/(?P<pk>[0-9]+)$', views.TextDelete.as_view(),
        name='text_delete'),
    url(r'^text/edit/(?P<pk>[0-9]+)$', views.TextUpdate.as_view(),
        name='text_edit'),
    url(r'^text/create/$', views.TextCreate.as_view(),
        name='text_create'),
    url(r'^textversions/$', views.TextVersionListView.as_view(), name='browse_textversions'),
    url(r'^textversion/detail/(?P<pk>[0-9]+)$', views.TextVersionDetailView.as_view(),
        name='textversion_detail'),
    url(r'^textversion/delete/(?P<pk>[0-9]+)$', views.TextVersionDelete.as_view(),
        name='textversion_delete'),
    url(r'^textversion/edit/(?P<pk>[0-9]+)$', views.TextVersionUpdate.as_view(),
        name='textversion_edit'),
    url(r'^textversion/create/$', views.TextVersionCreate.as_view(),
        name='textversion_create'),
]
