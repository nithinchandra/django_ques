from django.contrib import admin
from questions import models
# Register your models here.

admin.site.register(models.Question)
admin.site.register(models.Answer)
