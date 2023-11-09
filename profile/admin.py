from django.contrib import admin
from .models import *
from checkout.models import *
# Register your models here.

class Video_TabularInline(admin.TabularInline):
    model=Video
class course_admin(admin.ModelAdmin):
    inlines=(Video_TabularInline,)

"""class Checkout_TabularInline(admin.TabularInline):
    model=Checkout
class usercourse_admin(admin.ModelAdmin):
    inlines=(Checkout_TabularInline,)"""

admin.site.register(Course,course_admin)
admin.site.register(Instructor)
admin.site.register(Audience)
admin.site.register(Video)
admin.site.register(Content)
admin.site.register(UserCourse)
#admin.site.register(UserCourse,usercourse_admin)
