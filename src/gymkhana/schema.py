import graphene
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene import relay, Connection
from graphene_django import DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.views import GraphQLView
from photologue.models import Gallery
from festivals.schema import FestivalNode
from konnekt.schema import Query as KonnektQuery
from oauth.schema import UserProfileNode, UserNode
from main.schema import SocietyNode, ClubNode, GalleryNode
from counsellingTeam.schema import CounsellingTeamNode, FaqNode


class SearchResult(graphene.Union):
    class Meta:
        types = (UserProfileNode,)


class SearchResultConnection(Connection):
    class Meta:
        node = SearchResult


class NodeType(graphene.Enum):
    USER_PROFILE = UserProfileNode


class PublicQuery(graphene.ObjectType):
    node = relay.Node.Field()
    societies = DjangoFilterConnectionField(SocietyNode)
    clubs = DjangoFilterConnectionField(ClubNode)
    festivals = DjangoConnectionField(FestivalNode)
    counsellingTeam = DjangoFilterConnectionField(CounsellingTeamNode)
    faq = DjangoFilterConnectionField(FaqNode)
    home_carousel = graphene.Field(GalleryNode)
    home_gallery = graphene.Field(GalleryNode)

    def resolve_home_carousel(self, info, *args):
        return Gallery.objects.filter(slug=settings.HOME_PAGE_CAROUSEL_GALLERY_SLUG).first()

    def resolve_home_gallery(self, info, *args):
        return Gallery.objects.filter(slug=settings.HOME_PAGE_GALLERY_SLUG).first()


class PrivateQuery(KonnektQuery, PublicQuery):
    viewer = graphene.Field(UserNode)
    search = graphene.ConnectionField(
        SearchResultConnection,
        query=graphene.String(description='Value to search for', required=True),
        node_type=NodeType(required=True)
    )

    def resolve_viewer(self, info, *args):
        return UserNode.get_node(info, id=info.context.user.id)

    def resolve_search(self, info, query=None, node_type=None, first=None, last=None, before=None, after=None):
        # TODO: Add logic to paginate search based on first, last, before and after params
        if node_type == UserProfileNode:
            if first:
                return UserProfileNode.search(query, info)[:first]
            return UserProfileNode.search(query, info)
        return []


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    schema = graphene.Schema(PrivateQuery)


class PublicGraphQLView(GraphQLView):
    pass


schema = graphene.Schema(PublicQuery)
