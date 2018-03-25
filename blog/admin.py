from django.contrib import admin
from blog.models import Post,Category
class CategoryAdmin(admin.ModelAdmin):
 list_display= ('name','slug')
 prepulated_fields = {'sulg': ('name',)}
class PostAdmin(admin.ModelAdmin):
 list_display= ('title','slug')
 prepulated_fields = {'sulg': ('title',)}
 list_filter = ('title','slug','body','keywords')
 search_fields = ('title','body','keywords')
 prepulated_fields = {'sulg': ('title',)}
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)