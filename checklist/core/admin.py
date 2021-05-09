from django.contrib import admin
from .models import CheckList, CheckListItem

admin.site.register(CheckList)
admin.site.register(CheckListItem)