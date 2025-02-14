from django.contrib import admin
from .models import Hero_page,SocailLinks,About,Category,Skill

# Register your models here.
class Social_Link_Inline(admin.TabularInline):
    model = SocailLinks
    extra =1

class Hero_Admin(admin.ModelAdmin):
    list_display=('name','is_active')
    list_filter = ('is_active',)
    list_editable =('is_active',)
    search_fields =('name','des')
    inlines =[Social_Link_Inline]
admin.site.register(Hero_page, Hero_Admin)








class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'des', 'email', 'phone')
    search_fields = ('title', 'des', 'email', 'phone')
    inlines = [CategoryInline,SkillInline]
admin.site.register(About, AboutAdmin)