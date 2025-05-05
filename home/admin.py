from django.contrib import admin
from .models import (
    CompanyInfo, 
    Service, 
    Work, 
    CompanyStat, 
    Request, 
    PrivacyPolicy, 
    PersonalDataPolicy
)



admin.site.register(Service)
admin.site.register(Work)
admin.site.register(CompanyStat)
admin.site.register(Request)
admin.site.register(PrivacyPolicy)
admin.site.register(PersonalDataPolicy)


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('__str__',)



    