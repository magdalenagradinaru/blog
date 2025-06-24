#models.py:

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    active= models.BooleanField(default=True)


    def get_absolute_url(self):
        return reverse(
            'blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])


# Modelul Comment
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)                                                   #afișare în ordine cronologică

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)           #returnează o reprezentare textuală a comentariului cu autor și conținut


class Technology(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Project(models.Model):
    COMPLEXITY_CHOICES = [
        ('Simple', 'Simplu'),
        ('Medium', 'Mediu'),
        ('Complex', 'Complex'),
    ]
    slug = models.SlugField(unique=True, blank=True)  # Câmp slug
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', default='projects/default.jpg')
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_file = models.FileField(upload_to='project_files/', blank=True, null=True)
    score = models.DecimalField(max_digits=4, decimal_places=1, default=0.0)  # Notă între 0 și 10
    complexity_status = models.CharField(max_length=10, choices=COMPLEXITY_CHOICES, default='Simple')  # Status complexitate

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    author = models.CharField(max_length=100, verbose_name="Autor")
    date = models.DateField(verbose_name="Data")
    image = models.ImageField(upload_to='gallery/', verbose_name="Imagine")

    def __str__(self):
        return f"{self.author} - {self.date}"



class ResearchProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)  # Câmp opțional
    file = models.FileField(upload_to='research_projects/', blank=True, null=True)  # Câmp fișier
    created_at = models.DateTimeField(auto_now_add=True)  # Data creării
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='research_projects')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:private')


