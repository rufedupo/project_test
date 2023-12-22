import json
from django.shortcuts import render, redirect
from app.forms import ProjectForm
from datetime import datetime
from app.models import Project
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize

def project_view(request):
    form = ProjectForm()
    model = Project
    return render(request, 'project_template.html', {'model': model, 'form': form})

def get_projects_view(request):
    projects = Project.objects.all()
    projects_json = []
    for project in projects:
        projects_json.append({
            "id": project.id,
            "name": project.name,
            "created_at": project.created_at
        })
    return JsonResponse({'status': 'success', 'projects': projects_json})

def create_project_view(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

def delete_project_view(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project.delete()
    return JsonResponse({'status': 'success'})

def index_view(request):
    return render(request, 'index_template.html', {})