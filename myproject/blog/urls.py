from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('post/', views.project_index, name='project_index'),
    path('post/<int:pk>/', views.project_detail, name='project_detail'),
    path('add/', views.add_project, name='add_project'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('private/', views.private_view, name='private'),
    path('login/', views.login_or_register, name='login_or_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
