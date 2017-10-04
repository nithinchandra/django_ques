from django.conf.urls import url
from questions import views

app_name = 'questions'

urlpatterns = [
    url(r'^(\d+)/$', views.question, name='question'),
    url(r'^new/$', views.CreateQuestion.as_view(), name='create'),
    url(r'^answer/$', views.answer, name='answer'),
]
