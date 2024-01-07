from django.contrib import admin
from .models import *


# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio', 'get_html_photo']
    list_display_links = ['id', 'bio']
    search_fields = ('bio', )
    readonly_fields = ('get_html_photo', )

    def get_html_photo(self, object):
        return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото'


class MugsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_html_preview']
    list_display_links = ['id', 'title']
    search_fields = ('title', )

    def get_html_preview(self, object):
        return mark_safe(f'<img src="{object.preview.url}", width="50">')

    get_html_preview.short_description = 'Главное фото'


class ContestsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_html_photo']
    list_display_links = ['id', 'title']
    search_fields = ('title', )

    def get_html_photo(self, object):
        return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото'


class MasterclassesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_html_photo']
    list_display_links = ['id', 'title']
    search_fields = ('title', )

    def get_html_photo(self, object):
        return mark_safe(f'<img src="{object.photo.url}", width="50">')

    get_html_photo.short_description = 'Фото'


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Mugs, MugsAdmin)
admin.site.register(MugsPhotos)
admin.site.register(Contests, ContestsAdmin)
admin.site.register(Masterclasses, MasterclassesAdmin)

