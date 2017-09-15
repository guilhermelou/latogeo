from django.contrib import admin
from .models import Item, ItemSpec, ItemKind
# Register your models here.


class ItemKindAdmin(admin.ModelAdmin):
    model=ItemKind


class ItemSpecAdmin(admin.ModelAdmin):
    model=ItemSpec


class ItemAdmin(admin.ModelAdmin):
    model=Item


admin.site.register(ItemKind, ItemKindAdmin)
admin.site.register(ItemSpec, ItemSpecAdmin)
admin.site.register(Item, ItemAdmin)
