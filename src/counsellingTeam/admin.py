from django.contrib import admin
from .models import Team, FamilyTree


class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ('student_heads', 'student_assistant_heads', 'student_guides')


class FamilyTreeAdmin(admin.ModelAdmin):
    class Meta:
        model = FamilyTree


admin.site.register(Team, TeamAdmin)
admin.site.register(FamilyTree, FamilyTreeAdmin)
