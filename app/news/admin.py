from django.contrib import admin

from .models import ContentType
from .models import Category
from .models import News

# Register your models here.
admin.site.register(ContentType)
admin.site.register(Category)
admin.site.register(News)