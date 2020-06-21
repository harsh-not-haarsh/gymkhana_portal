import graphene
from graphene_django import DjangoObjectType

from .models import Team, FamilyTree
from oauth.schema import UserProfileNode
from oauth.models import UserProfile
from graphene_django import DjangoConnectionField


class CounsellingTeamNode(DjangoObjectType):
    class Meta:
        model = Team
        filter_fields = ['year', 'team_type']
        fields = ('__all__')
        interfaces = (graphene.relay.Node,)

    student_heads = UserProfileNode()
    student_assistant_heads = UserProfileNode()
    student_guides = UserProfileNode()


class FamilyTreeNode(DjangoObjectType):
    class Meta:
        model = FamilyTree
        filter_fields = ['id']
        fields = ('__all__')
        interfaces = (graphene.relay.Node,)

    mentees = DjangoConnectionField('counsellingTeam.schema.FamilyTreeNode')
    id = graphene.ID(required=True)

    def resolve_mentees(self, info):
        id=self.student_id
        user = UserProfile.objects.get(id=id)
        return user.mentees.all()

    def resolve_id(self, info):
        return self.student_id
