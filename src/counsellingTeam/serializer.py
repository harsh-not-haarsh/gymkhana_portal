from rest_framework import serializers

from oauth.models import UserProfile, SocialLink
from .models import Team


class UserProfileSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    skills_as_list = serializers.SerializerMethodField()
    social_links = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        exclude = ['user']

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_email(self, obj):
        return obj.user.email

    def get_skills_as_list(self, obj):
        return obj.skills_as_list

    def get_social_links(self, obj):
        handels = SocialLink.objects.filter(user=obj.user)
        data = {}
        for handel in handels:
            data[handel.social_media] = handel.link


class TeamSerializer(serializers.ModelSerializer):
    student_heads = UserProfileSerializer(many=True)
    student_assistant_heads = UserProfileSerializer(many=True)
    student_guides = UserProfileSerializer(many=True)

    class Meta:
        model = Team
        exclude = ['id']
