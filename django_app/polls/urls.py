from django.conf.urls import url
from . import views

urlpatterns = [
    # /polls/
    url(r'^$', views.index),
    # /pols/5
    url(r'^(?P<question_id>[0-9])+/S', views.detail, name='detail'),
    # /pols/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # /pols/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]