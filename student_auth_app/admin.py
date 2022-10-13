from django.contrib import admin
from student_auth_app.models import staff_tbl,student_tbl,course_tbl
# Register your models here.

admin.site.register(staff_tbl)
admin.site.register(student_tbl)
admin.site.register(course_tbl)