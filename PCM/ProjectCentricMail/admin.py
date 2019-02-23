from django.contrib import admin

# Register your models here.
from .models import MessageInfo,ProjectClassify,ProjectNames

admin.site.register(ProjectNames)
