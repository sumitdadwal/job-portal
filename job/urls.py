from django.urls import path
from . import views

urlpatterns = [
    path('create-job/', views.create_job, name='create-job'),
    path('update-job/', views.update_job, name='update-job'),
]