from django.contrib import admin

# Register your models here.

from .models import Article
from .models import User

admin.site.register([Article, User])
