import factory
from fixture.userfixture import UserProfileFactory


class FamilyTreeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'counsellingTeam.FamilyTree'

    student = factory.SubFactory(UserProfileFactory)
    student_guide = factory.SubFactory(UserProfileFactory)
