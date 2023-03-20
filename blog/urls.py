
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.PostDisplay.as_view(), name='blog'),
]