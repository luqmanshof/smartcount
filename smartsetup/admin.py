from django.contrib import admin
from smartsetup.models import UserProfile

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','user_info','city')
#
#     def user_info(self, obj):
#         return obj.description

# admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(UserProfile)
admin.site.site_header = 'SmartCOUNT Administration'
