from django.contrib import admin
from core.models import Lead, FAQ

class LeadAdmin(admin.ModelAdmin):
    list_display = ('added_on', 'name', 'email')

class FAQAdmin(admin.ModelAdmin):
    list_display = ('added_on', 'question', 'answer')

admin.site.register(Lead, LeadAdmin)
admin.site.register(FAQ, FAQAdmin)
