from django.contrib import admin
from .models import Film, Genre, Ticket, ProfileTickets, Profile, FilmComment
import datetime
from .services.admin_export import export_excel
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib.admin import SimpleListFilter

class FilmInstanceInline(admin.TabularInline):
    model = Ticket

# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', "view_genres_link")
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Рейтинг', {
            'fields': ('rating',)
        }),
    )
    search_fields = ('title',)
    date_hierarchy = "date_start_sales"
    inlines = [FilmInstanceInline]
    short_description = 'Фильмы'
    def save_execl(self, request, queryset):
        filename = 'media/{0}_{1}.xls'.format('amounts', datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        headers = [
            'ID', "Название", "duration"]
        columns = [
            'pk', 'title', 'short_description']
        return export_excel(queryset, headers, columns, filename)
    def view_genres_link(self, obj):
        from django.utils.html import format_html
        count = obj.genres.count()
        url = (
            reverse("admin:catalog_genre_changelist")
            + "?"
            + urlencode({"genre__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Жанра</a>', url, count)
    view_genres_link.short_description = "Жанры"

    save_execl.short_description = "Export to Excel"

    actions = [save_execl]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass

@admin.register(ProfileTickets)
class ProfileTicketsAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(FilmComment)
class FilmCommentAdmin(admin.ModelAdmin):
    pass