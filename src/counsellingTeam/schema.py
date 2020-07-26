from graphene import relay
from graphene_django import DjangoObjectType

from .models import Team, CsFaq, FamilyTree
from oauth.schema import UserProfileNode
from oauth.models import UserProfile
from graphene_django import DjangoConnectionField


class CounsellingTeamNode(DjangoObjectType):

    class Meta:
        model = Team
        filter_fields = ['year', 'team_type']
        fields = ('__all__')
        interfaces = (relay.Node,)

    student_heads = UserProfileNode()
    student_assistant_heads = UserProfileNode()
    student_guides = UserProfileNode()


class FaqNode(DjangoObjectType):

    class Meta:
        model = CsFaq
        filter_fields = ['category']
        fields = ('__all__')
        interfaces = (relay.Node,)


class FamilyTreeNode(DjangoObjectType):

    class Meta:
        model = FamilyTree
        filter_fields = ['student__roll']
        fields = ('__all__')
        interfaces = (relay.Node,)

    mentees = DjangoConnectionField('counsellingTeam.schema.FamilyTreeNode')

    def resolve_mentees(self, info):
        id = self.student_id
        user = UserProfile.objects.get(id=id)
        return user.mentees.all()
