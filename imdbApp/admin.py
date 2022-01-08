from django.contrib import admin
from .models import Movie,Category,Status,Language


# Register your models here.
admin.site.register(Movie)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(Status)
