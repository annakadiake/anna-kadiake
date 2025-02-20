from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, UserProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'gestion/register.html', {'form': form})

def profile_update(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'gestion/profile_update.html', {'form': form})
from .models import Project
from .forms import ProjectForm

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user  # Assurez-vous que l'utilisateur est connecté
            project.save()
            return redirect('project_list')  # Redirigez vers la liste des projets
    else:
        form = ProjectForm()
    return render(request, 'gestion/project_form.html', {'form': form})


from django.contrib.auth.decorators import login_required
from .models import Project

@login_required  # Ajoutez ce décorateur pour forcer l'authentification
def project_list(request):
    projects = Project.objects.filter(created_by=request.user)
    return render(request, 'gestion/project_list.html', {'projects': projects})
def project_update(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'gestion/project_form.html', {'form': form})

def project_delete(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'gestion/project_confirm_delete.html', {'project': project})
# gestion/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'gestion/home.html')  # Assurez-vous de créer ce template
# gestion/views.py
from django.shortcuts import render, redirect

from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('project_list')  # Redirigez vers la liste des projets ou une autre page
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'gestion/login.html')
# gestion/views.py
from django.shortcuts import render, get_object_or_404
from .models import Project

@login_required
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'gestion/project_detail.html', {'project': project})