# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from booking import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('enrollview', views.EnrollView.as_view(), name='enrollview'),
    path('enrollments', views.Enrollments.as_view(), name='enrollments'),
    path('enrollment_editing/<int:pk>',
          views.EditEnrolments.as_view(), name='enrollment_editing'),
]
