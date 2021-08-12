from django.urls import path

from . import views

urlpatterns = [
    # example : /polls/
    path("", views.index, name='index'),
    # example : /polls/1
    path('<int:question_id>/', views.detail, name='detail'),
    # example : /polls/1/results/
    path('<int:question_id>/results/', views.result, name='results'),
    # example : /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
