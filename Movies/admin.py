from django.contrib import admin
from Movies.models import Movies


class MoviesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Movies, MoviesAdmin)
