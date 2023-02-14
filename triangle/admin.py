from django.contrib import admin

from .models import Person, LoggerModel


@admin.register(LoggerModel)
class LoggerModelAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'path', 'method')
    fieldsets =(
    (None, {'fields': ['path', 'method']}),
    (None, {'fields': ['os', 'host']}),
    ("Date information", {'fields': ['timestamp']}),
    ('Body', {'fields': ['body'], 'classes': ['collapse']}),
    ('DATA', {'fields': ['data'], 'classes': ['collapse']}))

    list_filter = ['timestamp']
    search_fields = ['path']

    date_hierarchy = 'timestamp'
    actions_on_top = False
    actions_on_bottom = True

    list_display_links = ('path',)


admin.site.register(Person)
