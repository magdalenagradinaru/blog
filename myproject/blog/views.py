
from django.shortcuts import get_object_or_404
from .models import Post, Technology, GalleryImage
from .forms import CommentForm, ProjectForm, GalleryImageForm, ResearchProjectForm
from django.views.generic import ListView
from .models import Project
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })


def project_index(request):
    projects = Project.objects.all()
    technologies = Technology.objects.all()
    technology_id = request.GET.get('technology')
    if technology_id:
        projects = projects.filter(technology__id=technology_id)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:project_index')
    else:
        form = ProjectForm()
    return render(request, 'blog/project_index.html', {
        'projects': projects,
        'technologies': technologies,
        'form': form
    })

def add_project(request):
    technologies = Technology.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # Setează utilizatorul curent
            project.save()
            return redirect('blog:project_index')
    else:
        form = ProjectForm()
    return render(request, 'blog/add_project.html', {'form': form, 'technologies': technologies})


from django.shortcuts import render, redirect
from .models import ResearchProject
from django.contrib.auth.decorators import login_required

@login_required
def private_view(request):
    if request.method == 'POST':
        # Extragem datele din formular
        title = request.POST.get('title')
        description = request.POST.get('description')
        file = request.FILES.get('file')

        # Verificăm dacă datele sunt corecte
        if title and description:
            project = ResearchProject(
                title=title,
                description=description,
                file=file,
                author=request.user
            )
            project.save()  # Salvăm proiectul de cercetare

            return redirect('blog:private')  # Redirecționăm înapoi la aceeași pagină
    else:
        form = ResearchProjectForm()

    # Obținem proiectele de cercetare ale utilizatorului curent
    projects = request.user.research_projects.all()

    return render(request, 'blog/private.html', {
        'form': form,
        'projects': projects,
    })


@login_required
def custom_logout_view(request):
    logout(request)
    return redirect('/')

def login_or_register(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(data=request.POST)
        if auth_form.is_valid():
            user = auth_form.get_user()
            login(request, user)
            return redirect('blog:private')
        else:
            reg_form = UserCreationForm(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                username = reg_form.cleaned_data.get('username')
                password = reg_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('blog:private')
    else:
        auth_form = AuthenticationForm()
        reg_form = UserCreationForm()
    return render(request, 'blog/auth/login_or_register.html', {
        'auth_form': auth_form,
        'reg_form': reg_form,
    })



def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'blog/project_detail.html', {'project': project})


def gallery_view(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:gallery')
    else:
        form = GalleryImageForm()
    images = GalleryImage.objects.all()
    return render(request, 'blog/gallery.html', {'images': images, 'form': form})





