from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('employee/', views.EmployeeList.as_view(), name="employees"),
    path('employee/<slug:pk>', views.EmployeeDetails.as_view(), name="employee"),
    path('sector/', views.SectorList.as_view(), name="sectors"),
    path('sector/<slug:pk>', views.SectorDetails.as_view(), name="sector"),
    path('project/', views.ProjectList.as_view(), name="projects"),
    path('project/<slug:pk>', views.ProjectDetails.as_view(), name="project")
]

urlpatterns = format_suffix_patterns(urlpatterns)
