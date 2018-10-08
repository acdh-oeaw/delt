from django.contrib import admin
from .models import *


class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'assignment_desc_link', 'legacy_id', 'entered_by', 'entered_date', 'last_changed',
    )
    list_filter = ['title', 'entered_by']


class LearnerAdmin(admin.ModelAdmin):
    list_display = (
        'year_of_birth', 'lang_l', 'lang_father', 'lang_mother', 'lang_second', 'lang_third'
    )
    list_filter = ['gender', 'entered_by', 'year_of_birth']


class LearnerProfileAdmin(admin.ModelAdmin):
    list_display = (
        'learner_id', 'year', 'lang_spoken_home', 'lang_instruction_primary',
        'lang_instruction_secondary'
        )
    list_filter = ['year', 'lang_spoken_home']


class CourseGroupAdmin(admin.ModelAdmin):
    list_display = (
        'legacy_id', 'course_type', 'course_name', 'participants_no', 'school_studies_year',
        )
    list_filter = ['course_type', 'participants_no']


admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Learner, LearnerAdmin)
admin.site.register(LearnerProfile, LearnerProfileAdmin)
admin.site.register(CourseGroup, CourseGroupAdmin)
admin.site.register(Participant)
admin.site.register(Text)
admin.site.register(TextVersion)
