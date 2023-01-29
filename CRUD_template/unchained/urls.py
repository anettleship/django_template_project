from django.urls import path

from . import views

urlpatterns = [
    # example /unchained/
    path('', views.index, name='index'), 
    # example /unchained/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # example /unchained/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # example /unchained/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
