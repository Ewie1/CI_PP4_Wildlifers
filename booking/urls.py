# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from booking import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Urls to show enrollment create, list, edit, delete pages
urlpatterns = [
      path('enrollview', views.EnrollView.as_view(), name='enrollview'),
      path('enrollments',
           views.Enrollments.as_view(), name='enrollments'),
      path('enrollment_editing/<str:pk>',
           views.EditEnrollments.as_view(), name='enrollment_editing'),
      path('enrollment_cancel/<str:pk>',
           views.CancelEnrollments, name='enrollment_cancel'),
]
