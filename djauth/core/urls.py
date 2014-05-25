#encoding=utf-8
from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy


urlpatterns = patterns('core.views',
    url(r'^$', 'index', name='index'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'auth_account/login.html'},
        name='auth_login'),

    url(r'^logout/$', 'logout',
        {'template_name': 'auth_account/logout.html'},
        name='auth_logout'),

    url(r'^password/change/$', 'password_change',
        {'template_name': 'auth_account/password_change_form.html'},
        name='auth_password_change'),

    url(r'^password/change/done/$', 'password_change_done',
        {'template_name': 'auth_account/password_change_done.html'},
        name='auth_password_change_done'),

    url(r'^password/reset/$', 'password_reset',
        {
            'template_name': 'auth_account/password_reset_form.html',
            'email_template_name': 'auth_account/password_reset_email.html',
            'subject_template_name': 'auth_account/password_reset_subject.html',
            'post_reset_redirect': reverse_lazy('auth_password_reset_done'),
        },
        name='auth_password_reset'),

    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'password_reset_confirm', {
            'template_name':
            'auth_account/password_reset_confirm.html',
            'post_reset_redirect':
            reverse_lazy('auth_password_reset_complete')},
        name='auth_password_reset_confirm'),

    url(r'^password/reset/complete/$', 'password_reset_complete',
        {'template_name': 'auth_account/password_reset_complete.html'},
        name='auth_password_reset_complete'),

    url(r'^password/reset/done/$', 'password_reset_done',
        {'template_name': 'auth_account/password_reset_done.html'},
        name='auth_password_reset_done'),
)

