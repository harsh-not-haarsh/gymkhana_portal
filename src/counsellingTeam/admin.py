from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ('student_heads', 'student_assistant_heads', 'student_guides')


admin.site.register(Team, TeamAdmin)
