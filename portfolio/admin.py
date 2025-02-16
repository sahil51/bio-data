from django.contrib import admin
from .models import Hero_page,SocailLinks,About,Category,Skill,Projects,Resume, Expertise, Education, Certificate, ResSkill, Language, CustomCard,ContactMessage,ContactInfo

# Register your models here.

################################# main page ##################3
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

############################# about page #####################
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


########################################## resume ############
class ExpertiseInline(admin.TabularInline):
    model = Expertise
    extra = 1  

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1

class SkillInline(admin.TabularInline):
    model = ResSkill
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1

class CustomCardInline(admin.TabularInline):
    model = CustomCard
    extra = 1

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('main_title', 'main_description')  
    inlines = [ExpertiseInline, EducationInline, CertificateInline, SkillInline, LanguageInline, CustomCardInline]
admin.site.register(Resume,ResumeAdmin)

################################### project page ##############
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = (
        ('Project Details', {
            'fields': ('title', 'tech', 'des', 'live_link', 'source_code')
        }),
        ('Project Section Background', {
            'fields': ('background_image', 'background_video'),
            'description': "Set a background image or video for the entire Projects section."
        }),
    )

admin.site.register(Projects, ProjectAdmin)

############################# contact info ###########
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('heading',)
admin.site.register(ContactInfo,ContactInfoAdmin)

class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('name','email','message','submitted_at')
    list_display = ('name','email','message','submitted_at')

admin.site.register(ContactMessage,ContactMessageAdmin)