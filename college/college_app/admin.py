from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(StudentUser)
admin.site.register(TeacherUser)
@admin.register(Tenstudent)
class tenstudent(ImportExportModelAdmin):
    pass
@admin.register(Twelvestudent)
class twelvestudent(ImportExportModelAdmin):
    pass
@admin.register(Degreestudent)
class degreestudent(ImportExportModelAdmin):
    pass