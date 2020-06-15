from graphene import relay
from graphene_django import DjangoObjectType

from .models import Team
from oauth.schema import UserProfileNode


class CounsellingTeamNode(DjangoObjectType):

    class Meta:
        model = Team
        filter_fields = ['year', 'team_type']
        fields = ('__all__')
        interfaces = (relay.Node,)

    student_heads = UserProfileNode()
    student_assistant_heads = UserProfileNode()
    student_guides = UserProfileNode()
