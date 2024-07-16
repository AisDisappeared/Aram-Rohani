from django.contrib import admin
from .models import * 



class TagAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    list_filter = ['name']
    search_fields = ['name'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'



class CourseAdmin(admin.ModelAdmin):
    date_hierarchy = 'published_date'
    list_filter = ['title','tag']
    list_display = ['title','tag','views','published_date']
    search_fields = ['title'] 
    save_as = True
    save_on_top = True 
    search_help_text = f'search in: {". ".join(search_fields)}'




admin.site.register(Tag,TagAdmin)
admin.site.register(Course,CourseAdmin)