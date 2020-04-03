from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name="base"),
    path('charge', views.charge, name="charge"),
    path('success/<int:amount>', views.success_msg, name="success")
]