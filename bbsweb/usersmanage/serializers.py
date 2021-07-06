from rest_framework import serializers

from django.contrib.auth.models import User, Group

# from ..articles.models import Articles


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Articles.objects.all())

    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
