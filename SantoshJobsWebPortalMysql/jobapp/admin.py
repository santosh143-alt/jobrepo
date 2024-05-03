from django.contrib import admin
from jobapp.models import PuneJobs,BangloreJobs,ChennaiJobs,MumbaiJobs
# Register your models here.
class PuneJobAdmin(admin.ModelAdmin):
    list_display = ['date','company_name','title','eligibility','address','skills_required','experience','city','email','phone_number']
admin.site.register(PuneJobs,PuneJobAdmin)

class BangloreJobAdmin(admin.ModelAdmin):
    list_display = ['date','company_name','title','eligibility','address','skills_required','experience','city','email','phone_number']
admin.site.register(BangloreJobs,PuneJobAdmin)

class ChennaiJobAdmin(admin.ModelAdmin):
    list_display = ['date','company_name','title','eligibility','address','skills_required','experience','city','email','phone_number']
admin.site.register(ChennaiJobs,PuneJobAdmin)

class MumbaiJobAdmin(admin.ModelAdmin):
    list_display = ['date','company_name','title','eligibility','address','skills_required','experience','city','email','phone_number']
admin.site.register(MumbaiJobs,PuneJobAdmin)