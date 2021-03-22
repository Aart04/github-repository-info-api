from django.urls import path

from . import views

urlpatterns = [
    path('repository/<str:owner>/<str:repository_name>', views.RepositoryDetail.as_view()),
]