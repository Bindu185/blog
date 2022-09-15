from django.contrib import admin
from .models import library,author

# Register your models here.
class authorAdmin(admin.ModelAdmin):
    list_display=('name','gender','category')
    search_fields=('name',)
    list_filter=('category','gender',)

admin.site.register(library)
admin.site.register(author,authorAdmin)
