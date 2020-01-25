from django.contrib import admin
from .models import HTMuser

# Register your models here.


class HTMuserAdmin(admin.ModelAdmin):
    list_display = ('email', )


admin.site.register(HTMuser, HTMuserAdmin)
