# from django.shortcuts import render
from rest_framework import viewsets

from .models import Team
from .serializer import TeamSerializer


class TeamDisplayViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        year = self.request.GET.get('year')
        team_type = self.request.GET.get('team_type').upper()
        print(year, team_type)
        queryset = Team.objects.filter(year=year, team_type=team_type)
        print(len(queryset))
        return queryset
