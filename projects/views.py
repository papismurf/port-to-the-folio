from django.shortcuts import render
from .models import Project


def project_index(request):
    projects = Project.projects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = Project.projects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)
