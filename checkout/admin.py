from django.contrib import admin
from .models import *
from profile.models import *
# Register your models here.
"""class UserCourse_TabularInline(admin.TabularInline):
    model=UserCourse
class checkout_admin(admin.ModelAdmin):
    inlines=(UserCourse_TabularInline,)
admin.site.register(Checkout,checkout_admin)"""

admin.site.register(Checkout)
"""
class Video_TabularInline(admin.TabularInline):
    model=Video
class course_admin(admin.ModelAdmin):
    inlines=(Video_TabularInline,)

admin.site.register(Course,course_admin)
admin.site.register(Instructor)
admin.site.register(Audience)
admin.site.register(Video)
admin.site.register(Content)
admin.site.register(UserCourse)"""
