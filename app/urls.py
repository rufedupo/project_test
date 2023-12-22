from django.urls import path
from .views import (
    get_projects_view,
    create_project_view,
    delete_project_view, 
    project_view
)
from .views import index_view

urlpatterns = [
    path('projects/', project_view, name='project_view'),
    path('projects/all', get_projects_view, name='get_projects_view'),
    path('projects/create', create_project_view, name='create_project_view'),
    path('projects/<int:project_id>/delete', delete_project_view, name='delete_project_view'),
    path('', index_view, name='index_view')
]