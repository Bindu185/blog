from django.contrib import admin
from .models import Library,Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','email','gender')
    search_fields=('name','email')
    list_filter=('email','name','gender')

admin.site.register(Library)
admin.site.register(Author,AuthorAdmin)

