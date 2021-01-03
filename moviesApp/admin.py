from django.contrib import admin
from .models import Film, Contact

# Register your models here.
class searchAdmin(admin.ModelAdmin):
    search_fields = ('Title',)

admin.site.register(Film, searchAdmin)
admin.site.register(Contact)