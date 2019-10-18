from django.urls import path
from . import views

app_name = 'polls'

# The urls the templates will be rendered at
urlpatterns = [
    path('', views.index, name='index'),
    # passing the parameter, need to specify what parameter - in this case the primary key of the detail view
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]