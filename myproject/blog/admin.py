from django.contrib import admin
from .models import Post, Comment, Project, Technology, GalleryImage


#Modelele care vor fi integrate în panoul de administare
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status') #coloanele specificate în lista de obiecte
    list_filter = ('status', 'created', 'publish', 'author')                #panoul de filtrare din dreapta paginii
    search_fields = ('title', 'body')                                       #bara de cautare
    prepopulated_fields = {'slug': ('title',)}                              #să fie completat automat în baza titlului
    raw_id_fields = ('author',)                                             #in coloana autorul se afișează mai compact, după I|D
    date_hierarchy = 'publish'                                              #ordinare după dată
    ordering = ('status', 'publish')                                        #ordonare după status si publish


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')  # Coloanele de afișat pentru comentarii
    list_filter = ('active', 'created', 'updated')  # Filtre pentru comentarii
    search_fields = ('name', 'email', 'body')  # Căutare după nume, email și textul comentariilor
    actions = ['approve_comments', 'disable_comments']  # Acțiuni personalizate pentru administrarea comentariilor

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'created_at', 'score', 'complexity_status')  # Coloanele pentru proiecte
    list_filter = ('technology', 'created_at', 'complexity_status')                      # Filtre pentru proiecte
    search_fields = ('title', 'description')                                               # Căutare în titlu și descriere
    prepopulated_fields = {'slug': ('title',)}                                             # Pre-populare slug din titlu
    ordering = ('created_at',)                                                           # Ordine după data de creare

admin.site.register(Technology)  # Adaugă și tehnologia în admin


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'image', 'get_image_preview')
    list_filter = ('author', 'date')

    # Afisăm o previzualizare a imaginii
    def get_image_preview(self, obj):
        return f'<img src="{obj.image.url}" width="100" height="100"/>'

    get_image_preview.allow_tags = True